from typing import List

"""
最长的

二分法查找

https://labuladong.github.io/algo/di-yi-zhan-da78c/shou-ba-sh-48c1d/wo-xie-le--9c7a4/#%E4%BA%8C%E3%80%81%E5%AF%BB%E6%89%BE%E5%B7%A6%E4%BE%A7%E8%BE%B9%E7%95%8C%E7%9A%84%E4%BA%8C%E5%88%86%E6%90%9C%E7%B4%A2

https://zhuanlan.zhihu.com/p/440083790



"""


def solution(nums1: List[int], nums2: List[int]):
    """
    二分查找
    https://zhuanlan.zhihu.com/p/479958546
    """
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    nums1_length, nums2_length = len(nums1), len(nums2)
    left_pos, right_pos = 0, nums1_length
    half_len = (nums1_length + nums2_length + 1) // 2

    while left_pos <= right_pos:
        # 分割位置计算
        num1_i = (left_pos + right_pos) // 2
        # 二分查找
        # 数组 1 的分割位置
        num2_j = half_len - num1_i
        # 数组 2 的分割位置
        # 计算另一个数组中的位置

        # 边界条件判断
        if num1_i < nums1_length and nums2[num2_j - 1] > nums1[num1_i]:
            # 数组 1 的 分割 < 长度
            # 数组 2 的 右边区间最小 > 数据 1 的 左侧最大
            left_pos = num1_i + 1
        elif num1_i > 0 and nums1[num1_i - 1] > nums2[num2_j]:
            # 数组 1 的 分割位置 > 0
            # 数组 1 的 左侧最大 > 数组 2 的  右侧最小
            right_pos = num1_i - 1
        else:
            # 找到合适的划分

            # 计算左半部分的最大值
            if num1_i == 0:
                max_of_left = nums2[num2_j - 1]
            elif num2_j == 0:
                max_of_left = nums1[num1_i - 1]
            else:
                max_of_left = max(nums1[num1_i - 1], nums2[num2_j - 1])

            # 如果总长度为奇数，直接返回左半部分的最大值
            if (nums1_length + nums2_length) % 2 == 1:
                return max_of_left

            # 计算右半部分的最小值
            if num1_i == nums1_length:
                min_of_right = nums2[num2_j]
            elif num2_j == nums2_length:
                min_of_right = nums1[num1_i]
            else:
                min_of_right = min(nums1[num1_i], nums2[num2_j])

            # 返回左半部分的最大值和右半部分的最小值的平均值
            return (max_of_left + min_of_right) / 2


if __name__ == '__main__':
    print(solution([1, 2], [3, 4]))
    print(solution([1, 2], [3]))
