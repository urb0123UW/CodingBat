#!/usr/bin/env python3

def sum13(nums):
    if len(nums) == 0:
        return 0

    lucky_sum = 0
    for i in range(len(nums)):
        if i == 0 and nums[i] != 13:
            lucky_sum += nums[i]
        elif nums[i] != 13 and nums[i - 1] != 13:
            lucky_sum += nums[i]

    return lucky_sum