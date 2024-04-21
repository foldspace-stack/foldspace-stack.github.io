from typing import List

"""
两个链表
1. 构建链表
2. 
"""


class ListNode(object):
    val: int
    next: 'ListNode'

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        s = ""
        tmp = self
        while tmp is not None:
            s += "{0},".format(tmp.val)
            tmp = tmp.next
        return s


def listToChain(nums: List):
    head = ListNode(0)
    dy = head
    for index,i in enumerate(nums):
        dy.val = i
        if index < len(nums)-1:
            dy.next = ListNode(0)
            dy = dy.next
    return head


def chain2List(c: ListNode):
    _ = []
    dy = c
    while dy is not None:
        _.append(dy.val)
        dy = dy.next
    return _


def solution(chain1: ListNode, chain2: ListNode):
    """
    
    """
    head = ListNode(0)
    dy_head = head
    chain_1_dy = chain1
    chain_2_dy = chain2
    carry = 0
    while chain_1_dy or chain_2_dy:
        if chain_1_dy is None:
            val1 = 0
        else:
            val1 = chain_1_dy.val or 0
        if chain_2_dy is None:
            val2 = 0
        else:
            val2 = chain_2_dy.val or 0
        sum = carry + val1 + val2
        #dy_head.val = sum
        carry = sum // 10
        dy_head.next = ListNode(sum % 10)
        dy_head = dy_head.next
        if chain_1_dy is not None:
            chain_1_dy = chain_1_dy.next
        if chain_2_dy is not None:
            chain_2_dy = chain_2_dy.next
    if carry > 0:
        dy_head.next = ListNode(carry)
    return chain2List(head.next)


if __name__ == '__main__':
    l1 = [2,4,3]
    l2 = [5,6,4]
    chain1 = listToChain(l1)
    chain2 = listToChain(l2)
    print(chain1, chain2)
    print(chain2List(chain1), chain2List(chain2))
    
    _ = solution(chain1, chain2)
    print(l1, l2)
    print(_)
