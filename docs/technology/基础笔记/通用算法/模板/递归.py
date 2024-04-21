def recursion_func(params):
    def base_case_condition(params):
        pass

    def prepare_params(params):
        pass

    def construct_result(sub_problem_result):
        pass

    if base_case_condition(params):
        base_case_value=0
        return base_case_value

    new_params = prepare_params(params)

    sub_problem_result = recursion_func(new_params)
    result = construct_result(sub_problem_result)
    return result
