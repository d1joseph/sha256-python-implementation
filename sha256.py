# SHA 256 python implementation as a command line executable that encrypts input and
# returns a 256 bit length output has a hash digest.
# Inputs can be user data or media file types. Anything really.

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

# perform binary conversion for pre-processing 
def binary_conversion(raw_input):
    """
    Accepts a raw data input and converts to binary.
    """
    input_bin = ' '.join(format(i, 'b') for i in bytearray(raw_input, 'utf-8')).split(' ')

    print(input_bin)

def pad_bin_message(bin_message):
    """
    Accepts a binary representation as an array
    and pads with 0s until the data is a multiple
    of 512 less 64 bits.
    """
    
    return padded_bin_message

# main
def sha256(data_input):
    return hash_digest


if __name__ == "__main__":
    binary_conversion('hello world')