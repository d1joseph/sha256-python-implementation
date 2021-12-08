# run two concurrent loops and find a 
# matching sequence that exists in both loops
import random as r
import string as s
from sys import getsizeof


# generating dummy keys
def keyGen():
    char_pool = [char for char in s.ascii_letters]
    num_pool = [str(i) for i in range(0,10)]
    maxBitLength = 2048
    key = ''
    while getsizeof(key) <= maxBitLength:
        key += r.choice(char_pool + num_pool)
    
    return key


# 

if __name__ == "__main__":
    pass 
        