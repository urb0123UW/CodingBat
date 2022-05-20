#!/usr/bin/env python3

def xyz_there(str):
    #thinking of returning false if .xyz is in the string anywhere, but what if another xyz exists?

    for i in range( len (str) - 2):
        if str[i:i+3] == "xyz":

            if( i > 0 and str[i-1] != "."):
                return True
            elif i == 0:
                return True

    return False
