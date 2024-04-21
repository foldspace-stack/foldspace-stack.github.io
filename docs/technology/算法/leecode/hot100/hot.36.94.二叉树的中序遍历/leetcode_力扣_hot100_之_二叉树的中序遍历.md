# 题目

https://leetcode.cn/problems/binary-tree-inorder-traversal/description/?envType=featured-list&envId=2cktkvj?envType=featured-list&envId=2cktkvj

![](attachments/Pasted%20image%2020240308204913.png)

# 解题

递归写吧
```python
# Definition for a binary tree node.
from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(root: Optional[TreeNode]) -> List[int]:
    rst=[]
    if root is None:
        return rst
    def traver(root:Optional[TreeNode]):
        if root:
            traver(root.left)
            rst.append(root.val)
            traver(root.right)

    traver(root)
    return rst
        

```


也可以用栈道实现


```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    result = []
    stack = []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right
    return result

```