#!/usr/bin/env python3

def string_times(str, n):
    result = ""
    for i in range(n):
        result = result + str
        print (i)
    return result
  #  return str * n

  #result = ""
  #for i in range(n):  # range(n) is [0, 1, 2, .... n-1]
  #  result = result + str  # could use += here
  #return result