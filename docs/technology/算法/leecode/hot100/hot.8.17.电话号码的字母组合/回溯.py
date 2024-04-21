def solution(digits: list):
    KEY = {'2': ['a', 'b', 'c'],
           '3': ['d', 'e', 'f'],
           '4': ['g', 'h', 'i'],
           '5': ['j', 'k', 'l'],
           '6': ['m', 'n', 'o'],
           '7': ['p', 'q', 'r', 's'],
           '8': ['t', 'u', 'v'],
           '9': ['w', 'x', 'y', 'z']}
    rsts = []

    def backtrace(path, chooise_list):
        """
        chooise_list -> 12
        """
        if len(chooise_list)==0:
            rsts.append(path)
        else:
            for path_chooice in KEY[chooise_list[0]]:
                backtrace(path+path_chooice,chooise_list[1:])

    if digits:
        backtrace("", digits)
    return rsts
