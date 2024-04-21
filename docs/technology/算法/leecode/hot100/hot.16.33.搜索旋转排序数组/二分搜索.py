def solution(nums: list, target: int):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2 # 每次区间的中间值
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:  # target 在左边
            if nums[left] <= target <= nums[mid]:
                # 左边区间有序
                right = mid - 1
            else:
                left = mid + 1
        else:  # target 在右边
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
