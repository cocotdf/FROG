#include "ui.hpp"

#include <cstdlib>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <utility>

#include "json.hpp"

#ifdef _WIN32
#include <shellapi.h>
#include <winsock2.h>
#include <ws2tcpip.h>
#pragma comment(lib, "ws2_32.lib")
#else
#include <arpa/inet.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <unistd.h>
#endif

namespace frog::runtime {

namespace {

using frog::json::Object;

#ifdef _WIN32
using socket_t = SOCKET;
constexpr socket_t invalid_socket = INVALID_SOCKET;
#else
using socket_t = int;
constexpr socket_t invalid_socket = -1;
#endif

struct NetworkBootstrap {
    NetworkBootstrap() {
#ifdef _WIN32
        WSADATA data;
        if (WSAStartup(MAKEWORD(2, 2), &data) != 0) {
            throw std::runtime_error("WSAStartup failed.");
        }
#endif
    }
    ~NetworkBootstrap() {
#ifdef _WIN32
        WSACleanup();
#endif
    }
};

void close_socket(socket_t socket) {
    if (socket == invalid_socket) {
        return;
    }
#ifdef _WIN32
    closesocket(socket);
#else
    close(socket);
#endif
}

std::string read_text_file(const std::filesystem::path& path) {
    std::ifstream input(path, std::ios::binary);
    if (!input) {
        throw std::runtime_error("Unable to open file: " + path.string());
    }
    std::ostringstream buffer;
    buffer << input.rdbuf();
    return buffer.str();
}

std::string html_escape(const std::string& input) {
    std::string out;
    out.reserve(input.size());
    for (const char ch : input) {
        switch (ch) {
        case '&': out += "&amp;"; break;
        case '<': out += "&lt;"; break;
        case '>': out += "&gt;"; break;
        case '"': out += "&quot;"; break;
        case '\'': out += "&#39;"; break;
        default: out.push_back(ch); break;
        }
    }
    return out;
}

std::string property_string(const Object& properties, const std::string& key, const std::string& fallback = "") {
    const auto it = properties.find(key);
    if (it == properties.end() || !it->second.is_string()) {
        return fallback;
    }
    return it->second.as_string();
}

bool property_bool(const Object& properties, const std::string& key, bool fallback = false) {
    const auto it = properties.find(key);
    if (it == properties.end() || !it->second.is_bool()) {
        return fallback;
    }
    return it->second.as_bool();
}

std::uint16_t property_u16(const Object& properties, const std::string& key, std::uint16_t fallback = 0) {
    const auto it = properties.find(key);
    if (it == properties.end() || !it->second.is_number()) {
        return fallback;
    }
    const auto value = it->second.as_i64();
    if (value < 0 || value > 65535) {
        throw std::runtime_error("Widget value must remain in the u16 domain.");
    }
    return static_cast<std::uint16_t>(value);
}

struct Request {
    std::string method;
    std::string path;
    std::string body;
};

void send_all(socket_t client, const std::string& payload) {
    std::size_t sent = 0;
    while (sent < payload.size()) {
#ifdef _WIN32
        const int count = send(client, payload.data() + static_cast<int>(sent), static_cast<int>(payload.size() - sent), 0);
#else
        const ssize_t count = send(client, payload.data() + sent, payload.size() - sent, 0);
#endif
        if (count <= 0) {
            throw std::runtime_error("Failed to write to socket.");
        }
        sent += static_cast<std::size_t>(count);
    }
}

std::string receive_request(socket_t client) {
    std::string buffer;
    char chunk[4096];
    while (true) {
#ifdef _WIN32
        const int count = recv(client, chunk, sizeof(chunk), 0);
#else
        const ssize_t count = recv(client, chunk, sizeof(chunk), 0);
#endif
        if (count <= 0) {
            break;
        }
        buffer.append(chunk, chunk + count);
        if (buffer.find("\r\n\r\n") != std::string::npos) {
            const auto header_end = buffer.find("\r\n\r\n");
            const auto content_length_pos = buffer.find("Content-Length:");
            std::size_t content_length = 0;
            if (content_length_pos != std::string::npos) {
                const auto line_end = buffer.find("\r\n", content_length_pos);
                const auto value_begin = content_length_pos + std::string("Content-Length:").size();
                const auto raw_value = buffer.substr(value_begin, line_end - value_begin);
                content_length = static_cast<std::size_t>(std::stoul(raw_value));
            }
            if (buffer.size() >= header_end + 4 + content_length) {
                break;
            }
        }
    }
    return buffer;
}

Request parse_request(const std::string& raw) {
    const auto header_end = raw.find("\r\n\r\n");
    if (header_end == std::string::npos) {
        throw std::runtime_error("Malformed HTTP request.");
    }
    std::istringstream stream(raw.substr(0, header_end));
    Request request;
    stream >> request.method >> request.path;
    request.body = raw.substr(header_end + 4);
    return request;
}

void send_response(
    socket_t client,
    const std::string& status,
    const std::string& content_type,
    const std::string& body,
    const std::optional<std::pair<std::string, std::string>>& extra_header = std::nullopt) {
    std::ostringstream headers;
    headers << "HTTP/1.1 " << status << "\r\n";
    headers << "Content-Type: " << content_type << "\r\n";
    headers << "Content-Length: " << body.size() << "\r\n";
    headers << "Connection: close\r\n";
    if (extra_header.has_value()) {
        headers << extra_header->first << ": " << extra_header->second << "\r\n";
    }
    headers << "\r\n" << body;
    send_all(client, headers.str());
}

std::string url_decode(const std::string& input) {
    std::string output;
    output.reserve(input.size());
    for (std::size_t index = 0; index < input.size(); ++index) {
        const char ch = input[index];
        if (ch == '+') {
            output.push_back(' ');
        } else if (ch == '%' && index + 2 < input.size()) {
            const std::string hex = input.substr(index + 1, 2);
            output.push_back(static_cast<char>(std::stoi(hex, nullptr, 16)));
            index += 2;
        } else {
            output.push_back(ch);
        }
    }
    return output;
}

std::optional<std::string> parse_form_value(const std::string& body, const std::string& key) {
    std::size_t start = 0;
    while (start <= body.size()) {
        const auto end = body.find('&', start);
        const auto pair = body.substr(start, end == std::string::npos ? std::string::npos : end - start);
        const auto separator = pair.find('=');
        const std::string current_key = pair.substr(0, separator);
        const std::string current_value = separator == std::string::npos ? "" : pair.substr(separator + 1);
        if (current_key == key) {
            return url_decode(current_value);
        }
        if (end == std::string::npos) {
            break;
        }
        start = end + 1;
    }
    return std::nullopt;
}

void open_in_browser(const std::string& url) {
#ifdef _WIN32
    ShellExecuteA(nullptr, "open", url.c_str(), nullptr, nullptr, SW_SHOWNORMAL);
#elif __APPLE__
    std::string command = "open \"" + url + "\" >/dev/null 2>&1 &";
    std::system(command.c_str());
#else
    std::string command = "xdg-open \"" + url + "\" >/dev/null 2>&1 &";
    std::system(command.c_str());
#endif
}

} // namespace

BrowserUiRuntime::BrowserUiRuntime(
    std::optional<std::filesystem::path> contract_path,
    std::optional<std::filesystem::path> wfrog_path)
    : core(contract_path.value_or(default_contract_path()), wfrog_path.value_or(default_wfrog_path())) {}

std::string BrowserUiRuntime::render_html() const {
    const auto& ctrl = core.widgets.at("ctrl_input");
    const auto& ind = core.widgets.at("ind_result");
    const auto snapshot = frog::json::stringify(core.execution_artifact(), true, 2);

    const std::string ctrl_asset_url = ctrl.asset_id.has_value() ? "/asset/" + *ctrl.asset_id : std::string();
    const std::string ind_asset_url = ind.asset_id.has_value() ? "/asset/" + *ind.asset_id : std::string();
    std::string diagnostics;
    if (last_error.has_value()) {
        diagnostics = "<div class='diagnostic error'>" + html_escape(*last_error) + "</div>";
    }

    std::ostringstream html;
    html << "<!doctype html><html lang='en'><head><meta charset='utf-8'><title>" << html_escape(core.panel.title) << "</title>";
    html << "<style>"
            "body{font-family:Segoe UI,Arial,sans-serif;margin:24px;background:#f3f6f8;color:#1f2933;}"
            "h1{margin:0 0 12px 0;font-size:24px;}"
            "p.meta{margin:0 0 20px 0;color:#52606d;}"
            ".panel{width:460px;min-height:170px;background:#ffffff;border-radius:10px;padding:16px;box-shadow:0 4px 14px rgba(15,23,42,0.08);}"
            ".widgets{display:flex;gap:24px;align-items:flex-start;}"
            ".widget{width:180px;padding:12px;border-radius:8px;border:2px solid #cbd2d9;background:#fbfdff;}"
            ".widget img{display:block;width:100%;height:32px;object-fit:contain;margin-bottom:8px;}"
            ".widget label{display:block;margin-bottom:8px;font-size:12px;font-weight:600;text-transform:uppercase;letter-spacing:0.04em;}"
            ".widget input,.widget output{display:block;width:100%;padding:8px 10px;box-sizing:border-box;border-radius:6px;border:1px solid #9aa5b1;font-size:16px;}"
            ".widget output{background:#f8fff0;}"
            ".actions{margin-top:16px;display:flex;gap:12px;align-items:center;}"
            "button{padding:8px 14px;border:0;border-radius:6px;cursor:pointer;background:#0f62fe;color:#ffffff;font-weight:600;}"
            ".diagnostic{margin:12px 0;padding:10px 12px;border-radius:6px;}"
            ".diagnostic.error{background:#fff1f2;color:#9f1239;border:1px solid #fecdd3;}"
            "summary{cursor:pointer;margin-top:16px;font-weight:600;}"
            "pre{white-space:pre-wrap;word-break:break-word;background:#0b1020;color:#dbeafe;padding:12px;border-radius:8px;font-size:12px;}"
            "</style></head><body>";
    html << "<h1>" << html_escape(core.panel.title) << "</h1>";
    html << "<p class='meta'>Example 05 — contract + .wfrog + browser host runtime</p>";
    html << diagnostics;
    html << "<div class='panel'><form method='post' action='/run'><div class='widgets'>";
    html << "<section class='widget' style='border-color:" << html_escape(property_string(ctrl.properties, "foreground_color", "#5B9BD5")) << "'>";
    html << "<label>" << html_escape(property_string(ctrl.properties, "label", "Input")) << "</label>";
    if (!ctrl_asset_url.empty()) {
        html << "<img src='" << html_escape(ctrl_asset_url) << "' alt=''>";
    }
    html << "<input name='input_value' type='number' min='0' max='65535' value='" << property_u16(ctrl.properties, "value", 0) << "'";
    if (!property_bool(ctrl.properties, "enabled", true)) {
        html << " disabled";
    }
    html << ">";
    html << "</section>";

    html << "<section class='widget' style='border-color:" << html_escape(property_string(ind.properties, "foreground_color", "#70AD47")) << "'>";
    html << "<label>" << html_escape(property_string(ind.properties, "label", "Accumulated result")) << "</label>";
    if (!ind_asset_url.empty()) {
        html << "<img src='" << html_escape(ind_asset_url) << "' alt=''>";
    }
    html << "<output>" << property_u16(ind.properties, "value", 0) << "</output>";
    html << "</section></div>";
    html << "<div class='actions'><button type='submit'>Run Example 05</button><a href='/state.json'>state.json</a></div>";
    html << "</form><details><summary>Current runtime snapshot</summary><pre>" << html_escape(snapshot) << "</pre></details></div>";
    html << "</body></html>";
    return html.str();
}

void BrowserUiRuntime::serve(const std::string& host, std::uint16_t port, bool should_open_browser) {
    NetworkBootstrap network_bootstrap;
    (void)network_bootstrap;

    socket_t server = ::socket(AF_INET, SOCK_STREAM, 0);
    if (server == invalid_socket) {
        throw std::runtime_error("Unable to create server socket.");
    }

#ifndef _WIN32
    int opt = 1;
    setsockopt(server, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));
#endif

    sockaddr_in address{};
    address.sin_family = AF_INET;
    address.sin_port = htons(port);
    if (inet_pton(AF_INET, host.c_str(), &address.sin_addr) != 1) {
        close_socket(server);
        throw std::runtime_error("Only numeric IPv4 host values are supported by this minimal runtime.");
    }

    if (bind(server, reinterpret_cast<sockaddr*>(&address), sizeof(address)) != 0) {
        close_socket(server);
        throw std::runtime_error("Unable to bind server socket.");
    }
    if (listen(server, 16) != 0) {
        close_socket(server);
        throw std::runtime_error("Unable to listen on server socket.");
    }

    sockaddr_in bound_address{};
#ifdef _WIN32
    int bound_length = sizeof(bound_address);
#else
    socklen_t bound_length = sizeof(bound_address);
#endif
    if (getsockname(server, reinterpret_cast<sockaddr*>(&bound_address), &bound_length) != 0) {
        close_socket(server);
        throw std::runtime_error("Unable to inspect bound server socket.");
    }

    const std::string url = "http://" + host + ":" + std::to_string(ntohs(bound_address.sin_port)) + "/";
    std::cout << url << std::endl;
    if (should_open_browser) {
        open_in_browser(url);
    }

    while (true) {
        socket_t client = accept(server, nullptr, nullptr);
        if (client == invalid_socket) {
            continue;
        }
        try {
            const auto raw = receive_request(client);
            const auto request = parse_request(raw);
            if (request.method == "GET" && request.path == "/") {
                send_response(client, "200 OK", "text/html; charset=utf-8", render_html());
            } else if (request.method == "GET" && request.path == "/state.json") {
                send_response(client, "200 OK", "application/json; charset=utf-8", frog::json::stringify(core.execution_artifact(), true, 2));
            } else if (request.method == "GET" && request.path.rfind("/asset/", 0) == 0) {
                const std::string asset_id = request.path.substr(std::string("/asset/").size());
                const auto asset_it = core.asset_map.find(asset_id);
                if (asset_it == core.asset_map.end() || !std::filesystem::exists(asset_it->second)) {
                    send_response(client, "404 Not Found", "text/plain; charset=utf-8", "missing asset");
                } else {
                    send_response(client, "200 OK", "image/svg+xml", read_text_file(asset_it->second));
                }
            } else if (request.method == "POST" && request.path == "/run") {
                try {
                    const auto form_value = parse_form_value(request.body, "input_value").value_or("0");
                    const auto parsed = static_cast<std::uint16_t>(std::stoul(form_value));
                    core.execute(parsed);
                    last_error.reset();
                } catch (const std::exception& error) {
                    last_error = error.what();
                }
                send_response(client, "303 See Other", "text/plain; charset=utf-8", "", std::make_pair(std::string("Location"), std::string("/")));
            } else {
                send_response(client, "404 Not Found", "text/plain; charset=utf-8", "not found");
            }
        } catch (const std::exception& error) {
            send_response(client, "500 Internal Server Error", "text/plain; charset=utf-8", error.what());
        }
        close_socket(client);
    }
}

} // namespace frog::runtime
