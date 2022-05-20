#!/usr/bin/env python3

def count_code(str):
  code_cnt = 0
  
  for i in range(len(str) - 3):
    if( str[i:i+2] == "co" and str[i+3] == "e"):
      code_cnt +=1
      
  return code_cnt
