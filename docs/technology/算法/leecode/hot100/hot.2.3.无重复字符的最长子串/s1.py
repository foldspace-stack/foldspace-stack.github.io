from typing import List

"""
最长的

https://github.com/ascoders/weekly/blob/master/%E7%AE%97%E6%B3%95/199.%E7%B2%BE%E8%AF%BB%E3%80%8A%E7%AE%97%E6%B3%95%20-%20%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3%E3%80%8B.md


"""


def solution(s: str):
    """
    滑动窗口
    """
    rst = 0
    p_left = 0
    p_right = 0
    char_set = set()
    while p_right < len(s) and p_left < len(s):
        print('x,y', p_left, p_right,char_set,s[p_right])
        if p_right == len(s) - 1:
            break
        if s[p_right] not in char_set:
            rst = max(rst, p_right - p_left+1)
            print('p_right', p_right, 'rst:', rst)
            char_set.add(s[p_right])
            p_right += 1
        else:
            print('p_left', p_left)
            char_set.remove(s[p_left])
            p_left += 1
    return rst


if __name__ == '__main__':
    print(solution("abcabcbb"))
