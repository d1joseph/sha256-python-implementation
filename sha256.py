#!/usr/bin/python

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
                This code is written and intended for educational purposes only and
                should not be implemented in anything resembling a production
                environment.
                Algorithm spec can be found here:
                # http://csrc.nist.gov/publications/fips/fips180-2/fips180-2withchangenotice.pdf

"""
__author__ = 'Dhiv Joseph'
__licence__ = 'MIT'
import copy
import struct
import binascii


# hash constants (h) - 8 hash values of the first 32 bits of the fractional parts of the
# square roots of the first 8 primes: 2, 3, 5, 7, 11, 13, 17, 19.
h = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0xa54ff53a,
    0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x1f83d9ab, 0x5be0cd19]
# round constants (k) - 64 hash values representing the first 32 bits of the fractional parts
# of the cube roots of the first 64 primes (2 - 311).
k = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]


# pre-processing raw data into 512 bit message blocks for message digesting in the scheduler.
def pre_process(raw_data):
    """
    Process raw message parameter as a 512 bit message block.
    >>> pre_process('hello world')
    >>> 0110100001100101011011000110110001101111001000000111011101101111011100100110110001100100
    """

    # raw_value converted to binary representation as a string and append a 1 as separator.
    msg = ''.join(format(i, '08b') for i in bytearray(raw_data, encoding='utf-8')) + '1'
    # add zeroes for padding to until message block is evenly divisible by 512.
    # reserve 64 bits on the end to encode the len of original message. 
    
    while len(msg) % (512) != 0:
        msg += '0'
    
    print(f'Original message: {raw_data}')
    print(f'Current message block bit length: {len(msg)}')


# main
def sha256(data_input):
    pass


# WIP
# 1. optimize pre-process routine and validate output for step 2 (meets message block properties) 
# 2. message schedule routine
# 3. compression function main loop
# 4. operators routine
# 5. structure main algo class
# 6. write tests using NIST test specs
# 7. testing with pytest
# 8. Pep8 everything
# 9. cmdlet module
# 10. test cmdlet use cases
# 11. setup tools and package
# 12. final tests
# 13. deploy


if __name__ == "__main__":
    pre_process('hello world')