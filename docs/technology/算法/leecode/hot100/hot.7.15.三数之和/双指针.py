def soultion(nums: list):
    rsts = []
    nums = sorted(nums)
    for i in range(len(nums)):
        if nums[i] > 0:
            return rsts
        # 去重
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left_p = i + 1
        right_p = len(nums) - 1
        while left_p < right_p:
            sum_ = nums[i] + nums[left_p] + nums[right_p]
            if sum_ > 0:
                right_p -= 1
            elif sum_ < 0:
                left_p += 1
            else:
                _ = [nums[i], nums[left_p], nums[right_p]]
                print(nums, i, left_p, right_p)
                rsts.append(_)
                """
                消除重复
                """
                while right_p > left_p and nums[right_p] == nums[right_p - 1]:
                    right_p -= 1
                while right_p > left_p and nums[left_p] == nums[left_p + 1]:
                    left_p += 1
                left_p += 1
                right_p -= 1
    return rsts


if __name__ == '__main__':
    s = soultion([-1, 0, 1, 2, -1, -4])
    print(s)
    s=soultion([0,0,0])
    print(s)
