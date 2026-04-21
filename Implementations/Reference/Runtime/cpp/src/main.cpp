#include <cstdint>
#include <filesystem>
#include <iostream>
#include <optional>
#include <stdexcept>
#include <string>
#include <vector>

#include "execute.hpp"
#include "json.hpp"
#include "ui.hpp"

namespace {

std::string require_value(const std::vector<std::string>& args, std::size_t& index, const std::string& option_name) {
    ++index;
    if (index >= args.size()) {
        throw std::runtime_error("Missing value for option " + option_name + ".");
    }
    return args[index];
}

} // namespace

int main(int argc, char** argv) {
    try {
        std::vector<std::string> args;
        args.reserve(static_cast<std::size_t>(argc > 0 ? argc - 1 : 0));
        for (int index = 1; index < argc; ++index) {
            args.emplace_back(argv[index]);
        }

        if (!args.empty() && args.front() == "ui") {
            args.erase(args.begin());
            std::optional<std::filesystem::path> contract_path;
            std::optional<std::filesystem::path> wfrog_path;
            std::string host = "127.0.0.1";
            std::uint16_t port = 0;
            bool open_browser = true;

            for (std::size_t index = 0; index < args.size(); ++index) {
                if (args[index] == "--contract") {
                    contract_path = require_value(args, index, "--contract");
                } else if (args[index] == "--wfrog") {
                    wfrog_path = require_value(args, index, "--wfrog");
                } else if (args[index] == "--host") {
                    host = require_value(args, index, "--host");
                } else if (args[index] == "--port") {
                    port = static_cast<std::uint16_t>(std::stoul(require_value(args, index, "--port")));
                } else if (args[index] == "--no-open-browser") {
                    open_browser = false;
                } else {
                    throw std::runtime_error("Unknown ui argument: " + args[index]);
                }
            }

            frog::runtime::BrowserUiRuntime runtime(contract_path, wfrog_path);
            runtime.serve(host, port, open_browser);
            return 0;
        }

        std::optional<std::filesystem::path> contract_path;
        std::optional<std::filesystem::path> wfrog_path;
        std::uint16_t input_value = 3;

        if (!args.empty() && args.front() == "run") {
            args.erase(args.begin());
        }
        if (!args.empty() && !args.front().starts_with("--")) {
            input_value = static_cast<std::uint16_t>(std::stoul(args.front()));
            args.erase(args.begin());
        }

        for (std::size_t index = 0; index < args.size(); ++index) {
            if (args[index] == "--contract") {
                contract_path = require_value(args, index, "--contract");
            } else if (args[index] == "--wfrog") {
                wfrog_path = require_value(args, index, "--wfrog");
            } else {
                throw std::runtime_error("Unknown argument: " + args[index]);
            }
        }

        const auto artifact = frog::runtime::execute_contract(input_value, contract_path, wfrog_path);
        std::cout << frog::json::stringify(artifact, true, 2) << std::endl;
        return 0;
    } catch (const std::exception& error) {
        std::cerr << error.what() << std::endl;
        return 1;
    }
}
