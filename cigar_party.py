#!/usr/bin/env python3

def cigar_party(cigars, is_weekend):
    if(cigars >= 40 and is_weekend ):
        return True
    elif(cigars >= 40 and cigars <=60 and not is_weekend ):
        return True
    else:
        return False


  #if is_weekend:
  #  return (cigars >= 40)
  #else:
  #  return (cigars >= 40 and cigars <= 60)

