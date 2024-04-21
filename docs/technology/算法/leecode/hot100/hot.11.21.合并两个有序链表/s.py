from typing import List
from collections import deque

"""
最长的

https://github.com/ascoders/weekly/blob/master/%E7%AE%97%E6%B3%95/199.%E7%B2%BE%E8%AF%BB%E3%80%8A%E7%AE%97%E6%B3%95%20-%20%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3%E3%80%8B.md


"""


class TreeNode(object):
    val: int
    next: 'TreeNode'

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def solution(nums1: TreeNode, nums2: TreeNode):
    """
    滑动窗口
    """
    if nums1 is None:
        return nums2
    if nums2 is None:
        return nums1
    p_1 = nums1
    p_2 = nums1
    dy=None
    while p_1 is not None and p_2 is not None:
        if p_1.val <= p_2.val:
            dy= p_2
            dy.next=p_1.next
            p_1.next=dy
            p_1=dy.next
            p_2=p_2.next
        else:
            dy 
    rst = []

    return rst


if __name__ == '__main__':
    assert solution("(]") == False
    assert solution("()[]{}") == True
