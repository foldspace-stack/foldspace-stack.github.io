from typing import *


def solution(height: List[int]):
    """
    当前索引能存的水量为 前面>当前 和右边 > 当前 中最小的数-当前的高度
    """
    if len(height) < 3: return 0  # 数组长度小于3，不可能积水，返回0
    left, right = 0, len(height) - 1  # 初始化左右指针
    left_max, right_max = height[left], height[right]  # 初始化左右最高墙的高度
    water_trapped = 0  # 初始化积水总量
    while left < right:  # 当左指针小于右指针时，循环
        if left_max < right_max:  # 左边的最高墙低于右边的最高墙
            left += 1  # 移动左指针
            left_max = max(left_max, height[left])  # 更新左边的最高墙高度
            water_trapped += left_max - height[left]  # 累加积水量
        else:  # 右边的最高墙低于或等于左边的最高墙
            right -= 1  # 移动右指针
            right_max = max(right_max, height[right])  # 更新右边的最高墙高度
            water_trapped += right_max - height[right]  # 累加积水量
    return water_trapped  # 返回积水总量
