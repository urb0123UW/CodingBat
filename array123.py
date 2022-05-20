#!/usr/bin/env python3

def array123(nums):
    length = len(nums)
    for i in range (length - 2):
        if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
            return True
    return False