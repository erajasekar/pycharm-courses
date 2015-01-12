from test_helper import run_common_tests, failed, passed, import_task_file

def check_result(student_answer, answer, input_desc):
    if student_answer == answer:
        passed(input_desc)
    else:
        failed("", input_desc)

if __name__ == '__main__':
    run_common_tests()
    function = import_task_file().sum_double
    check_result(function(1,2), 3, "sum_double(1, 2) -> 3")
    check_result(function(3,2), 5, "sum_double(3, 2) -> 5")
    check_result(function(-1,0), -1, "sum_double(-1, 0) -> -1")
    check_result(function(2,2), 8, "sum_double(2, 2) -> 8")
    check_result(function(3,3), 12, "sum_double(3, 3) -> 12")
    check_result(function(0,0), 0, "sum_double(0, 0) -> 0")
    check_result(function(0,1), 1, "sum_double(0, 1) -> 1")
    check_result(function(3,4), 7, "sum_double(3, 4) -> 7")


