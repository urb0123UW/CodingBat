#!/usr/bin/env python3

def front_back(str):
    if len(str) > 1:
        save = str[1:-1]
        return str[-1] + save + str[0]
    else:
        return str

  #first = str[0]
  #last = str[-1]
  #str[0] = last
  #str[-1] = first
  #return str
