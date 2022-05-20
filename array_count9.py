#!/usr/bin/env python3

def array_count9(nums):
    count_9 = 0
    for i in range(len(nums)):
        if nums[i] == 9:
            count_9 +=1

    return count_9