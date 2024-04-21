from typing import List

"""
两个链表
1. 构建链表
2. 
"""


def solution(chain1: List[int], chain2: List[int]):
    """
    
    """
    l1_head_i = 0
    l2_headr_i = 0
    d1 = 0
    d2 = 0
    next_add = 0
    r = []
    while d1 < len(chain1) or d2 < len(chain2) or next_add > 0:
        item1 = 0
        item2 = 0
        if d1 < len(chain1):
            item1 = chain1[d1]
        if d2 < len(chain2):
            item2 = chain2[d2]
        sum_current = item1 + item2 + next_add
        r.append(sum_current % 10)
        next_add = sum_current // 10
        d1 += 1
        d2 += 1
    return r


if __name__ == '__main__':
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    _ = solution(l1, l2)
    print(l1, l2)
    print(_)
    _ = solution([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9])
    print(_)
    assert _ == [8, 9, 9, 9, 0, 0, 0, 1]
