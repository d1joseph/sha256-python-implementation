# SHA 256 python implementation as a command line executable that encrypts input and
# returns a 256 bit length output has a hash digest.
# Inputs can be user data or media file types. Anything really.
from sys import getsizeof as gso


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


# pre-processing raw data to get 512 bit message block. 
def pre_process(raw_message):
    """
    Accepts a raw message data and converts to a 512 bit message block.
    """
    # binary conversion
    byte_array = bytearray(raw_message, 'utf-8')
    bin_message = ['0' + bin(byte)[2:] for byte in byte_array]
    bin_message.append('1')
    

    # padding
    return bin_message


# main
def sha256(data_input):

    # hash constants (h) - 8 hash values of the first 32 bits of the fractional parts of the
    # square roots of the first 8 primes: 2, 3, 5, 7, 11, 13, 17, 19.
    h0 = 0x6a09e667
    h1 = 0xbb67ae85
    h2 = 0x3c6ef372
    h3 = 0xa54ff53a
    h4 = 0x510e527f
    h5 = 0x9b05688c
    h6 = 0x1f83d9ab
    h7 = 0x5be0cd19

    # round constants (k) - 64 hash values representing the first 32 bits of the fractional parts
    # of the cube roots of the first 64 primes (2 - 311).
    k = [
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
        0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
        0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2,
    ]

    pass


# WIP
# 1. finish pre-process routine
# 2. write message schedule routine
# 3. write compression routine
# 4. write operators routine
# 5. structure main algo class
# 6. write tests using NIST test specs
# 7. testing with pytest
# 8. Pep8 everything
# 9. cmdlet module
# 10. test cmdlet use cases
# 11. setup tools and package
# 12. deploy


if __name__ == "__main__":
    pass