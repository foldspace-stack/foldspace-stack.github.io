# 题目

https://leetcode.cn/problems/validate-binary-search-tree?envType=featured-list&envId=2cktkvj?envType=featured-list&envId=2cktkvj

![](attachments/Pasted%20image%2020240308211929.png)

# 解题

这个 感觉 递归就行

```python
from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode = left
        self.right: TreeNode = right


def solution(root: Optional[TreeNode]) -> bool:

    def helper(node, lower=float('-inf'), upper=float('inf')):
        if not node:
            return True
        val = node.val
        if val <= lower or val >= upper:
            return False
        if not helper(node.right, val, upper):
            return False
        if not helper(node.left, lower, val):
            return False
        return True

    return helper(root)

```

