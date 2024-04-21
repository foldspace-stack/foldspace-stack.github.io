from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution(lists: List[Optional[ListNode]]):
    def merge_two_list(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        f_node: ListNode = ListNode(None)
        dy: ListNode = f_node
        while list1 and list2:
            if list1.val < list2.val:
                dy.next = list1
                list1 = list1.next
            else:
                dy.next = list2
                list2 = list2.next
            dy = dy.next
        dy.next = list1 and list1 or list2
        return f_node.next

    if len(lists) < 1:
        return None
    if len(lists) == 1:
        return lists[0]
    mid = len(lists) // 2
    l1 = solution(lists[:mid])
    l2 = solution(lists[mid:])
    return merge_two_list(l1, l2)
