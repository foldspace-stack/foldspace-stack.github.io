from typing import *


def solution(nums: List[int]):
    sum_max = nums[0]
    current_sum = nums[0]
    for num in nums[1:]:
        """
        -2
        1 -> -1,-2 -> -1  
        -3 -> 
        4
        -1
        """
        current_sum = max(num, current_sum + num)
        sum_max = max(current_sum, sum_max)
    return sum_max
