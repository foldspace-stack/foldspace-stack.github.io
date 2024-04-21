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
        
