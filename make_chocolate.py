#!/usr/bin/env python3

def make_chocolate(small, big, goal):

    if( small + big * 5 < goal ):
        return -1

    big_needed = int(goal / 5)
    if ( big_needed > big ):
        big_needed = big

    small_needed = goal - (big_needed * 5)

    if small < small_needed:
        return -1

    return small_needed