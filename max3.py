#!/usr/bin/env python3

def max3(nums):
  larger = max(nums[0], nums[2])
  for i in range(len(nums)):
    nums[i] = larger
  return nums

