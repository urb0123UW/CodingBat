#!/usr/bin/env python3

def count_hi(str):
    hicount = 0
  
    for i in range(len(str)):
        if( i != len(str) - 1 ):
        
            if( str[i] + str[i+1] == "hi"):
                hicount +=1
          
    return hicount

#codingbat solution, note that they limited the range of the loop instead of adding
#an if check, also they sliced the string
def count_hi2(str):
    sum = 0
    ## Loop to length-1 and access index i and i+1
    ## in the loop.
    for i in range(len(str)-1):
        if str[i:i+2] == 'hi':
            sum = sum + 1
    return sum

def cat_dog(str):
  cat_cnt = 0
  dog_cnt = 0

  for i in range(len(str) - 2):
    if str[i:i+3] == "cat":
      cat_cnt += 1
    elif  str[i:i+3] == "dog":
      dog_cnt += 1

  if( cat_cnt == dog_cnt):
    return True
  else:
    return False
