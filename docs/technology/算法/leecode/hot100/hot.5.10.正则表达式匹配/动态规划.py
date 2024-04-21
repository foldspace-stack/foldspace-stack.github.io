def solution(target_str: str, regx_pattern: str):
    str_length = len(target_str)
    regx_length = len(regx_pattern)

    def init_dp():
        dp = [[False for i in range(0, regx_length + 1)] for j in range(str_length + 1)]
        dp[0][0] = True
        return dp

    dp = init_dp()

    def stats_transition(dp, i, j, target_str: str, regx_pattern: str):
        """
        1. 
        """
        if not dp[i - 1][j - 1]:
            return False
        regx_index = j - 1
        str_index = i - 1
        """
        1. aaa abcd*
        """
        if regx_pattern[regx_index] == '*':
            """
            a*a
            aa
            
            
            """
            return dp[i][j-2] or dp[i-1][j]
        elif regx_pattern[regx_index] == '.':
            return True
        else:
            return target_str[str_index] == regx_pattern[regx_index]

    for i in range(0, str_length + 1):
        for j in range(1, regx_length + 1):
            print('range', i, j,dp)
            dp[i][j] = stats_transition(dp, i, j, target_str, regx_pattern)
    return dp[str_length][regx_length]

if __name__ == '__main__':
    s = solution("aaaaa", 'a*')
    print(s)
