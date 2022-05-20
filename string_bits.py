#!/usr/bin/env python3

def string_bits(str):
    retval = ""
    for i in range(len(str)):
        if i % 2 == 0:
            retval += str[i]

    return retval

    #i = 0;
    #retval = ""
    #for c in str:
    #    if i%2==0:
    #        retval += c
    #    i += 1
    #return retval

    #for i in range(len(str)):
    #if i % 2 == 0:
    #  result = result + str[i]
  #return result