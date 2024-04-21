# 题目

![[Pasted image 20240229185944.png]]

# 解题

分析
链表问题 倒数第 n 个
1. 需要先确定 要删除的位置
2. 执行删除操作
3. 执行操作
很容易想到暴力求解 主要循环两次
1. 一次得到长度
2. 得到位置

## 暴力


```python
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

```


# 双指针

1. 一个指针 先走 n 
2. 再两个指针一起走
主要用了 技巧 不直接算 n 

```python
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

```