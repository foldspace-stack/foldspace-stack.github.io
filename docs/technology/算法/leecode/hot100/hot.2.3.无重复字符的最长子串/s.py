from typing import List

"""
最长的

https://github.com/ascoders/weekly/blob/master/%E7%AE%97%E6%B3%95/199.%E7%B2%BE%E8%AF%BB%E3%80%8A%E7%AE%97%E6%B3%95%20-%20%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3%E3%80%8B.md


"""


def solution(s: str):
    """
    滑动窗口
    """
    char_index_map = {}
    n = len(s)
    ans = 0
    left, right = 0, 0
    while right < n:
        right_val = s[right]
        if right_val in char_index_map:
            # 如果字符已经在窗口中出现过，则更新左指针位置
            # 出现过 重复条件不成立, 重新计算 最长度
            # 
            left = max(char_index_map[right_val] + 1, left)
        char_index_map[right_val] = right
        # 更新最长子串的长度
        ans = max(ans, right - left + 1)
        # 移动右指针
        right += 1
    return ans


if __name__ == '__main__':
    print(solution("abcabcbb"))
