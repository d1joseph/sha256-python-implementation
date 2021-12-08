#!/usr/bin/python

# A python implementation of the SHA256 hash algorithm as a command line executable that takes a parameter input (data) and
# returns the 256 bit length output has a hash digest.
# I wrote this as a learning exercise to better understand cryptopgrahic hash functions and primitives.

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
                environment, application or encryption method.
                
                The NIST algorithm spec can be found here:
                # http://csrc.nist.gov/publications/fips/fips180-2/fips180-2withchangenotice.pdf

                This algorithm was tested according the NIST standard. 

"""

__author__ = 'Dhiv Joseph'
__licence__ = 'MIT'
<<<<<<< HEAD:sha256.py

=======
import copy
import struct
import binascii
from tests.keys import keyGen
# TESTS
# print(keyGen())
>>>>>>> 04218c2d40a64219907df70161fdabdac06579c0:app/sha256.py

# hash constants (h) - 8 hash values of the first 32 bits of the fractional parts of the
# square roots of the first 8 primes: 2, 3, 5, 7, 11, 13, 17, 19.
H = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0xa54ff53a,
    0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x1f83d9ab, 0x5be0cd19]

# round constants (k) - 64 hash values representing the first 32 bits of the fractional parts
# of the cube roots of the first 64 primes (2 - 311).
K = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]

class SHA256:

<<<<<<< HEAD:sha256.py
    def __init__(self):
        pass
=======
# pre-process the raw data into 512 bit message blocks (chunks) to digest and moved into the scheduler.
def pre_process(raw_data):
    """
    """
    # raw value converted to binary representation as a string
    msg = ''.join(format(i, '08b') for i in bytearray(raw_data, encoding='utf-8'))
>>>>>>> 04218c2d40a64219907df70161fdabdac06579c0:app/sha256.py

    
    def translation(self, message):
        """
        """
        charcodes = [ord(c) for c in message]
        
        bytes = []
        for char in charcodes:
            bytes.append(bin(char)[2:].zfill(8))
        
        bits = []
        for byte in bytes:
            for bit in byte:
                bits.append(int(bit))

        return bits

    # utility function - base conversion
    def base_conversion(self, value):
        """
        """
        value = ''.join([str(x) for x in value])

        binaries = []
        for d in range(0, len(value), 4):
            binaries.append('0b' + value[d:d+4])

        hexes = ''
        for b in binaries:
            hexes += hex(int(b, 2))[2:]
        
        return hexes

    # utility function - base zero filler
    def zero_fill(self, bits, length=8, endian='LE'):
        """
        """
        l = len(bits)
        
        if endian == 'LE':
            for i in range(1, length):
                bits.append(0)
        
        else:
            while l < length:
                bits.insert(0, 0)
                l = len(bits)
        
        return bits

    # utility function - chunk messages into 512 bit chunks
    def chunker(self, bits, chunk_length=8):
        """
        """
        chunked = []
        for b in range(0, len(bits), byte_length):
            chunked.append(bits[b:b+byte_length])

        return chunked

    # initialize values
    def initializer(self, values):
        """
        """
        binaries = [bin(int(v, 16))[2:] for v in values]
        words = []
        for binary in binaries:
            word = []
            for b in binary:
                word.append(int(b))
            words.append(zero_zill(word, 32, 'BE'))
    
<<<<<<< HEAD:sha256.py
=======
    # std outputs
    print(f'Original data: {raw_data}\nType: {type(raw_data)}\n')
    print(f'Message converted to binary: \n{msg}\n')
    print(f'Message block bit length: {len(msg_block)}')


# main
def sha256(data_input):
    """
    """
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
>>>>>>> 04218c2d40a64219907df70161fdabdac06579c0:app/sha256.py

    # message preparation
    def pre_process_message(message):
        """
        """
        

if __name__ == "__main__":
    sha = SHA256()
    
