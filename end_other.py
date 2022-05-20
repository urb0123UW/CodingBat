#!/usr/bin/env python3

def end_other(a, b):
    la = a.lower()
    lb = b.lower()
    retval = False

    if( la == lb[-len(la):]):
        retval = True

    if( lb == la[-len(lb):]):
        retval = True

    return retval

#CodingBat solution.... endswith!!!???
def end_other2(a, b):
  a = a.lower()
  b = b.lower()
  return (b.endswith(a) or a.endswith(b))
