#!/usr/bin/env python3

def string_match(a, b):
    matches = 0
    for i in range(len(a) - 1):
        two_char_a = a[i:i+2]
        for n in range( len(b) - 1):
            two_char_b = b[n:n+2]
            if( two_char_a == two_char_b and i == n):
                matches +=1
    return matches

