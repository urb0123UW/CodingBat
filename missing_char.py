#!/usr/bin/env python3

def missing_char(str, n):
    if len(str) > n:
        beginning = str[0:n]
        end = str[n+1:]
        return beginning + end
    else:
        return str
