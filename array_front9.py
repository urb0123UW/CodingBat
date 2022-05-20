#!/usr/bin/env python3

def array_front9(nums):
    length = 0
    if len(nums) > 4:
        length = 4
    else:
        length = len(nums)

    if 9 in nums[0:length]:
        return True
    else:
        return False
    # First figure the end for the loop
    #end = len(nums)
    #if end > 4:
    #    end = 4

    #for i in range(end):  # loop over index [0, 1, 2, 3]
    #    if nums[i] == 9:
    #    return True
    #return False