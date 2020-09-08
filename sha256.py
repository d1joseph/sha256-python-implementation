# SHA 256 implementation. A command line executable that crypto encrypts inputs
# Inputs can be user data input or media file types. Anything really.

"""
* Filename:   sha256.py
* Author:     Dhiv Joseph
* Copyright:
* Disclaimer:   This code is presented 'as is' without any guarantees.
* Description:  Implementation of the SHA-256 hashing algorithm as a cmdlet.
                SHA-256 is one of the three algorithms in the SHA2 spec.
                The others, SHA-384 and SHA-512, are not included.
                Algorithm spec can be found here:
                # http://csrc.nist.gov/publications/fips/fips180-2/fips180-2withchangenotice.pdf

"""

import sys
import os
import math


# prime number generator function
def generate_primes(start_int=int(input('Start integer: ')), stop_int=int(input('Stop integer: '))):
    """
    Generates a list of prime numbers given a start and stop value.

    """
    prime_nums = []
    for Number in range(start_int, stop_int):
        count = 0
        for i in range(2, (Number // 2 + 1)):
            if(Number % i == 0):
                count = count + 1
                break
        if(count == 0 and Number != 1):
            prime_nums.append(Number)
    return prime_nums


# binary converter function
def convert_to_bin(k, format=True):
    """
    Converts a list of integers to binary.

    The first parameter, k, is the interger list.
    The second optional parameter, format, enables formatting.
    This is enabled by default.
    Set format=False to disable formatting.
    Binary output will then begin with '0b'.

    """
    k_bin = []
    if format:
        for i in range(len(k)):
            k[i] = bin(k[i]).replace('0b', '')
            k_bin.append(k[i])
    else:
        for i in range(len(k)):
            k[i] = bin(k[i])
            k_bin.append(k[i])
    return k_bin


# binary shift right 32 function
