from typing import *


def solution(nums: List[int]):
    # 确定问题的解空间
    max_reach=0
    for i in range(len(nums)):
        if i > max_reach: # 当前的位置 > 最大可大的位置
            return False # 直接
        max_reach = max(max_reach, i + nums[i]) #当前位置+ 之前最远的位置 
    return max_reach >= len(nums) - 1
        