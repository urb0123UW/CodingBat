#!/usr/bin/env python3

def sum67(nums):
    if len(nums) == 0:
        return 0

    total = 0
    skip = False
    for num in nums:
        if num == 6:
            skip = True

        if skip == False:
            total += num

        if( skip == True and num == 7):
            skip = False

    return total