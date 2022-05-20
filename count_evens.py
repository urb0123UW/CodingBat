#!/usr/bin/env python3

def count_evens(nums):
    evens = 0;
    for n in nums:
        if n % 2 == 0:
            evens += 1

    return evens