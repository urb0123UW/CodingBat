#!/usr/bin/env python3

def diff21(n):
    if n > 21:
        return abs(21 - n ) * 2
    else:
        return 21 - n