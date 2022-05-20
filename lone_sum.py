#!/usr/bin/env python3

def lone_sum(a, b, c):
  if a == b and b == c:
    return 0
    
  if a == b:
    return c

  if a == c:
    return b
    
  if b == c:
    return a
    
  return a + b + c

    #def lone_sum(a, b, c):
    #sum = 0
    #if a != b and a != c: sum += a
    #if b != a and b != c: sum += b
    #if c != a and c != b: sum += c
  
    #return sum
  