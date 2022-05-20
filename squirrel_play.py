#!/usr/bin/env python3
def squirrel_play(temp, is_summer):
  if is_summer and temp <= 100 and temp >=60 :
    return True
  elif not is_summer and temp <= 90 and temp >= 60:
    return True
  else:
    return False
