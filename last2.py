#!/usr/bin/env python3

def last2(str):
    if len(str) < 2:
        return 0

    found = 0
    sub_string = str[-2:]
    for i in range (len(str) - 2):
        if( sub_string == str[i:i+2] ):
            found += 1

    return found