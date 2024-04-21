from typing import List
from collections import deque

"""
最长的

https://github.com/ascoders/weekly/blob/master/%E7%AE%97%E6%B3%95/199.%E7%B2%BE%E8%AF%BB%E3%80%8A%E7%AE%97%E6%B3%95%20-%20%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3%E3%80%8B.md


"""


def solution(s: str):
    """
    滑动窗口
    """
    if len(s) <= 1:
        return True
    i = 0
    stack = deque()
    rst = True
    e_map = {
        '{': '}',
        "[": ']',
        "(": ")"
    }
    while i < len(s):
        if s[i] in e_map.keys():
            stack.append(s[i])
        elif s[i] in e_map.values():
            rst = rst and e_map[stack.pop()] == s[i]
        i += 1
    print(rst)
    return rst


if __name__ == '__main__':
    assert solution("(]") == False
    assert solution("()[]{}") == True
