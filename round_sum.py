#!/usr/bin/env python3

def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)

def round10(n):
    remainder = n % 10
    if( remainder == 0 ):
        return n

    if( remainder < 5 ):
        return n - remainder

    return n - remainder + 10