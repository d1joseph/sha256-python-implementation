# sha256-python-implementation

## Why I wrote this?
A Saturday afternoon fun project. I wanted to learn more about cryptographic hash functions and thought writing
a pure implementation could be a fun way to do so. I used this NIST paper http://csrc.nist.gov/publications/fips/fips180-2/fips180-2withchangenotice.pdf as my basis for the specification.

This is my pure python implementation of the SHA256 hash algorithm. Hopefully this repo helps others in their learning of
SHA algorithms and it's inner workings.

## About SHA256
A member of the SHA2 family of security functions, SHA256 is a cryptographic one-way hash function which returns a 256 bit length digest. It is a keyless hash function which is a standard known as [MDC](https://en.wikipedia.org/wiki/MDC-2) (Manipulation Detection Code). A slight change in the input will produce a significant difference in the resulting digest.

**For example**  
`SHA256("The quick brown fox jumps over the lazy dog")`  
`>>> d7a8fbb307d7809469ca9abcb0082e4f8d5651e46d3cdb762d02d0bf37c9e592`

**Same input with a period at the end**  
`SHA256("The quick brown fox jumps over the lazy dog.")`  
`>>> ef537f25c895bfa782526529a9b63d97aa631564d5d789c2b765448c8635fb6c`

This behaviour is due the [avalanche effect](https://en.wikipedia.org/wiki/Avalanche_effect), a desirable characteristic in cryptographic hashing which reduces poor randomization thus lowering input predicability given only the output.

The algorithm is structured as a [Merkle-Damgård](https://en.wikipedia.org/wiki/Merkle%E2%80%93Damg%C3%A5rd_construction) contruct and inputs processed via a one-way function built using a [Davies-Meyer](https://en.wikipedia.org/wiki/One-way_compression_function#Davies%E2%80%93Meyer) structure.

Ultimately a cryptographic hash function has 3 key properties:
1. Is determinisctic in that some data input will always produce the same output unique to that input.
2. Accepts input of arbitrary length and returns a fixed length output, 256 bits in the case of SHA256.
3. Is one-way in that the input cannot be derived from the output.

## Verification 
This implementation of the SHA256 algorithm aims to meet verifiability through demonstrating machine-checked proofs for functional correctness, of side-channel restistance, of information-flow properties (A.Appel, 2015 Verification of a Cryptographic Primitive: SHA-256).

## Operations and Constants
The formal algorithm spec includes a set of operations and functions we need to utilize on word chunks and some constant variables we need to initialise.

### Basic Operations:
- Bools = AND, XOR, OR
- We perform addition modulo 2^32, denoted by A + B. This constrains the integer to 32 bit range
- RotR(A, n) =  denotes the circular right shift on N bits of the binary word A.
- ShR(A, n) =  denotes the right shift on N bits of the binary word A.
- A||B denotes the concatenation of the binary words A and B.

### Bitwise Operations:
- Ch(X, Y, Z) = (X ^ Y) XOR (X~ Z),
- Maj(X, Y, Z) = (X ^ Y) XOR (X ^ Z) XOR (Y ^ Z),
- UpperSigma(X) = RotR(X, 2)  XOR RotR(X, 13) XOR RotR(X, 22),
- UpperSigma(X) = RotR(X, 6) XOR RotR(X, 11) XOR RotR(X, 25),
- LowerSigma(X) = RotR(X, 7) XOR RotR(X, 18) XOR ShR(X, 3) <- rotate xor shift right
- LowerSigma(X) = RotR(X, 17) XOR RotR(X, 19) XOR ShR(X, 10) <- rotate xor shift right

### Constants
- round constants(k)
- hash constants (h) 
- message schedule (w)

## General Step-By-Step
1. Pre-processing
2. Initialise hash values (h)
3. Initialise round constants (k)
4. Chunk loop - 512 bit messsage blocks to run through scheduler
5. Message schedule (w) - breaksdown blocks in the 32 bit arrays (words). See https://qvault.io/cryptography/how-sha-2-works-step-by-step-sha-256/ for a really good explanation of how this step works in detail
7. Compression
8. Modify final values
9. Concatenate final hash!
