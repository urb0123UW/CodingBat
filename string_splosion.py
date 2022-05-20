#!/usr/bin/env python3

def string_splosion(str):
    retval = ""
    for i in range(len(str) + 1):
        retval += str[0:i]

    return retval