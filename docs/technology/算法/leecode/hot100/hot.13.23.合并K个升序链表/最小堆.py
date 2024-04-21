from typing import *
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __lt__(self, other):
        return self.val < other.val


def solution(lists: List[Optional[ListNode]]):
    min_heap=[]
    for l in lists:
        if l:
            heapq.heappush(min_heap, l)
    f_node=ListNode(0)
    dy=f_node
    while min_heap:
        node = heapq.heappop(min_heap)
        dy.next=node
        if node.next:
            heapq.heappush(min_heap,node.next)
        dy=dy.next
    return f_node.next
    
    
