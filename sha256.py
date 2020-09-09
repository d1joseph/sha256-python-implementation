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

# components of SHA256

# To note:
# Bools = AND, XOR, OR
# We perform addition modulo 2**32, denoted by A + B. This contrains the integer to
# 32 bit range
# RotR(A, n) =  denotes the circular right shift on N bits of the binary word A.
# ShR(A, n) =  denotes the right shift on N bits of the binary word A.
# A||B denotes the concatenation of the binary words A and B.

# functions - bitwise operations

# Ch(X, Y, Z) = (X ^ Y) XOR (X~ Z),
# Maj(X, Y, Z) = (X ^ Y) XOR (X ^ Z) XOR (Y ^ Z),
# UpperSigma(X) = RotR(X, 2)  XOR RotR(X, 13) XOR RotR(X, 22),
# UpperSigma(X) = RotR(X, 6) XOR RotR(X, 11) XOR RotR(X, 25),
# LowerSigma(X) = RotR(X, 7) XOR RotR(X, 18) XOR ShR(X, 3) <- rotate xor shift right
# LowerSigma(X) = RotR(X, 17) XOR RotR(X, 19) XOR ShR(X, 10) <- rotate xor shift right

# consts = 64 binary words K**i given by the first 32 bits of the fractional parts
# of the cube roots of the first 64 prime numbers. 

