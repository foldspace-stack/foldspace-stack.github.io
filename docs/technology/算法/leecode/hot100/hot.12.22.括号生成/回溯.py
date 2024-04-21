def solution(n: int):
    rsts = []

    def backtrace(path, left: int, right):
        if len(path) == n * 2:
            """
            退出递归条件
            """
            rsts.append(path)
            return
        if left < n:
            """
            分之 1 加左括号
            """
            backtrace(path + "(", left + 1, right)
        if right < left:
            """
            右括号次数 < 左括号  可以加
            """
            backtrace(path + ")", left, right + 1)

    # for i in range(n):
    backtrace("", 0, 0)
    return rsts
