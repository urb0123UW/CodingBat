#!/usr/bin/env python3

def centered_average(nums):

    return ( int ((sum(nums) - min(nums) - max(nums) ) / (len(nums) - 2)) )

    #cent_average = (sum(nums) - min(nums) - max(nums) ) / (len(nums) - 2)
    #return int(cent_average)