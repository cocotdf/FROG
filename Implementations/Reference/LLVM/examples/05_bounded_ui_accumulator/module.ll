; FROG example 05 - first LLVM-native closure

@fmt_state = private unnamed_addr constant [16 x i8] c"final_state=%d\0A\00"
@fmt_output = private unnamed_addr constant [18 x i8] c"public_output=%d\0A\00"
@fmt_status = private unnamed_addr constant [10 x i8] c"status=ok\0A\00"

declare i32 @printf(ptr, ...)
declare i32 @atoi(ptr)

define i16 @frog_example05_accumulate(i16 %input_value) {
entry:
  %mul = mul i16 %input_value, 5
  ret i16 %mul
}

define i32 @main(i32 %argc, ptr %argv) {
entry:
  %has_arg = icmp sgt i32 %argc, 1
  br i1 %has_arg, label %parse_arg, label %use_default

parse_arg:
  %argv1ptr = getelementptr inbounds ptr, ptr %argv, i64 1
  %argv1 = load ptr, ptr %argv1ptr, align 8
  %parsed = call i32 @atoi(ptr %argv1)
  %trunc = trunc i32 %parsed to i16
  br label %run

use_default:
  br label %run

run:
  %input_value = phi i16 [ %trunc, %parse_arg ], [ 3, %use_default ]
  %result = call i16 @frog_example05_accumulate(i16 %input_value)
  %result_i32 = sext i16 %result to i32

  %fmt_state_ptr = getelementptr inbounds [16 x i8], ptr @fmt_state, i64 0, i64 0
  call i32 (ptr, ...) @printf(ptr %fmt_state_ptr, i32 %result_i32)

  %fmt_output_ptr = getelementptr inbounds [18 x i8], ptr @fmt_output, i64 0, i64 0
  call i32 (ptr, ...) @printf(ptr %fmt_output_ptr, i32 %result_i32)

  %fmt_status_ptr = getelementptr inbounds [10 x i8], ptr @fmt_status, i64 0, i64 0
  call i32 (ptr, ...) @printf(ptr %fmt_status_ptr)

  ret i32 0
}
