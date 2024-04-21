def solution(s: str):
    """
    1. 子问题
    """
    str_length = len(s)
    rst = s[0]
    max_length = 1
    global_map = {
        'rst': rst,
        'max_length': max_length
    }
    if str_length <= 1:
        return s

    def initialize_dp(problem):
        """
        dp[left][right]=True 表示是一个回文字符串 
        """
        problem_length = len(problem)
        return [[False for i in range(0, problem_length)] for j in range(0, problem_length)]

    def stats_transition(dp, left_i, right_j, problem, global_map):
        """
        内面的是回文字 无需再判断
        """
        if problem[left_i] == problem[right_j] and (right_j - left_i <= 2 or dp[left_i + 1][right_j - 1]):
            dp[left_i][right_j] = True
            cur_length = right_j - left_i + 1
            if cur_length > global_map['max_length']:
                global_map['max_length'] = cur_length
                global_map['rst'] = problem[left_i:right_j+1]

    def construct_result(dp, problem, global_map):
        """
        """
        return global_map['rst']

    dp = initialize_dp(s)
    """
    确定遍历顺序
    保证 所有都是经过计算的, 需要先计算
    1. 从被依赖的计算
    """
    for i in reversed(range(0, len(dp))):
        for j in range(i,len(dp)):
            #print('i,j',i,j)
            stats_transition(dp, i, j, s, global_map)
            #print(dp)
    solution = construct_result(dp, s, global_map)
    return solution


if __name__ == '__main__':
    c = solution("aacabdkacaa")
    print(c)
    print('exit')
