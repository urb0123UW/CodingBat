#!/usr/bin/env python3

def pos_neg( a, b, negative):
    if negative:
        return (a < 0 and b < 0)
    else:
        return (a > 0 and b < 0) or (a < 0 and b > 0)

#    if negative == True:
#        if(a < 0 and b < 0):
#            return True
#        else:
#            return False
#    elif negative == False:
#        if (a > 0 and b < 0) or (a < 0 and b > 0):
#            return True
#        else:
#            return False
#    else:
#        return False

# suggested solution
  #if negative:
  #  return (a < 0 and b < 0)
  #else:
  #  return ((a < 0 and b > 0) or (a > 0 and b < 0))