#!/usr/bin/env python3

def close_far(a, b, c):
    retval = False

    if (abs(a - b) < 2):

        if( abs(a - c) > 1 and abs(b - c) > 1 ):
            retval = True

    if( abs(a - c) < 2):

        if( abs(a - b) > 1 and abs(b - c) > 1 ):
            retval = True

    return retval;