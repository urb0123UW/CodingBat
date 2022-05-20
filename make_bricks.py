#!/usr/bin/env python3

def make_bricks(small, big, goal):
    #not enough brick length
    if small + big * 5 < goal:
        return False



    #enough brick length
    #need to figure out how many of the big bricks we need to use
    float_max_big = goal / 5
    int_max_big = (int)(float_max_big)

    num_small_needed = (float_max_big - int_max_big) * 5

    if small >= num_small_needed:
        return True
    else:
        return False


# mod solution
#    if small < goal % 5:
#        return False
#    else:
#        return True