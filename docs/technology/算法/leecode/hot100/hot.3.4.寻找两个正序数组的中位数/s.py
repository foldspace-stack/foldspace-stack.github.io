from typing import List

"""
最长的回文字
"""


def solution(nums1: List[int], num2: List[int]):
    """
    滑动窗口
    """
    m = nums1 + num2
    print(m)
    m.sort()
    if len(m) % 2 == 0:
        _ = m[len(m) // 2 -1:len(m) // 2+1 ]
        print("sl",_)
        return sum(_) / 2
    else:
        return m[len(m) // 2 ]


if __name__ == '__main__':
    print(solution([1, 2], [3, 4]))
    print(solution([1, 2], [3]))
    