#!/usr/bin/env python3

def has22(nums):
    retval = False

    for i in range( len(nums) - 1):
        if nums[i] == 2 and nums[i+1] == 2:
            retval = True

    return retval