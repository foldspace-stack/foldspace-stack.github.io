from typing import *


def solution(nums: List[int]):
    """
    回溯法
    路径 
    """
    rst = []
    length = len(nums)
    visited = [False for i in range(length)]

    def backtrack(path, chooice_list):
        """
        位置为 i 时候的排列情况
        """
        if len(path) >= len(chooice_list):
            rst.append(path[:])
            return
        for i in range(len(chooice_list)):
            if not visited[i]:
                visited[i] = True # 标记是否走过
                path.append(nums[i]) # 路径组合+
                backtrack(path,chooice_list) # 前进一步
                path.pop() # 回退一步
                visited[i] = False

    backtrack([],nums)
    return rst
