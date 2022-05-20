#!/usr/bin/env python3

def front3(str):
    if( len(str) < 3 ):
        n = len(str)
    else:
        n = 3
    three = str[0:n]
    return 3 * three