#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time    : 2023/7/15 01:17
# @author  : timger/yishenggudou
from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution(head: Optional[ListNode], n: int):
    """
    双指针
    """
    dy: ListNode = ListNode(next=head)
    first: ListNode = dy
    second: ListNode = dy
    i = 0
    while i <= n:
        i += 1
        first = first.next
    while first:
        first = first.next
        second = second.next
    second.next = second.next.next
    return dy.next
