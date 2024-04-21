from typing import List


def solution(s: str):
    """
    dp[i] 表示 i 个字符串的 匹配长度
    """

    def init_dp()->List[int]:
        return [0 for i in range(len(s))]

    if len(s) < 2 or s is None:
        return 0

    def state_trans(dp, i, s):
        """
        dp[i]=dp[i-2]+2
        """
        if s[i] == ')':
            if i - 1 >= 0 and s[i - 1] == "(":
                dp[i] = dp[i - 2] + 2
            elif s[i - 1] == ")" and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                dp[i] = (dp[i - 1] + dp[i - dp[i - 1] - 2]) + 2

    #
    #test
    dp: List[int] = init_dp()
    print(dp)
    for i in range(len(s)):
        state_trans(dp, i, s)
    return max(dp)


if __name__ == '__main__':
    s = ")()())"
    print(solution(s))
    s = "()"
    print(solution(s))
