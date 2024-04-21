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
    length = 0
    first: ListNode = head
    while first:
        length += 1
        first = first.next
    d = length - n
    first = dy
    while d > 0:
        first = first.next
        d -= 1
    first.next = first.next.next
    return dy.next
