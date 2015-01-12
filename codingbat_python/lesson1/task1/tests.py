from test_helper import run_common_tests, failed, passed, get_answer_placeholders, import_task_file


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if placeholder == "return a+b":  # TODO: your condition here
        passed()
    else:
        failed()

def check_result(student_answer, answer, input_desc):
    if student_answer == answer:
        passed(input_desc)
    else:
        failed("", input_desc)

if __name__ == '__main__':
    run_common_tests()
    #test_answer_placeholders()
    function = import_task_file().sum_double
    check_result(function(1,2), 3, "sum_double(1, 2) -> 3")
    check_result(function(2,2), 8, "sum_double(2, 2) -> 8")


