from test_framework import generic_test


# # First solution
# def parity(x: int) -> int:
#     bitCount = 0
#     while x :
#         bitCount += x & 1
#         x >>= 1
#     return bitCount % 2

# # Solution 1A on my own using a lookup table for each byte.
# def parity(x:int) -> int:
#     bitCount = 0
#     lookupTable = [computeParity(i) for i in range(1<<8)]
#     while x :
#         bitCount += lookupTable[x & ((1<<8) -1)]
#         x >>= 8
#     return bitCount % 2
#
# def computeParity(x : int) -> int :
#     bitCount = 0
#     while x :
#         bitCount += x & 1
#         x >>= 1
#     return bitCount % 2

# # Solution 2 using the trick to remove the least set bit
# def parity(x: int) -> int:
#     bitCount = 0
#     while x :
#         bitCount ^= 1
#         x &= x-1
#     return bitCount

# # Solution 2A using the trick to remove the least set bit and a lookup table
# def parity(x: int) -> int:
#     bitCount = 0
#     lookupTable = [computeParity(i) for i in range(1 << 8)]
#     while x:
#         bitCount ^= lookupTable[x & ((1 << 8) - 1)]
#         x >>= 8
#     return bitCount
#
#
# def computeParity(x: int) -> int:
#     bitCount = 0
#     while x:
#         bitCount ^= 1
#         x &= x - 1
#     return bitCount

# # Solution 3 that makes use of continually parallelizing XORing the bits in the number.
def parity_XOR(x: int) -> int:
    x ^= (x >> 32)
    x ^= (x >> 16)
    x ^= (x >> 8)
    x ^= (x >> 4)
    x ^= (x >> 2)
    x ^= (x >> 1)
    return x & 0x1


# Solution 3A that makes use of continually parallelizing XORing the bits in the number and cachng 16 bit word results.
def computeParity(x: int, word_size: int) -> int:
    # expect word size to be a power of 2
    while word_size:
        x ^= (x >> word_size)
        word_size >>= 1
    return x & 0x1


PARITY_LOOKUP_TABLE = [computeParity(i, 8) for i in range(2 ** 16)]


def parity(x: int) -> int:
    x ^= (x >> 32)
    x ^= (x >> 16)
    return PARITY_LOOKUP_TABLE[x & (2 ** 16 - 1)]

# # REDO problem
# # compute the parity for the first 2**(i+1) bits in n
# def computeParity(n: int, i: int) :
#     while i >= 0 :
#         n ^= n >> (2**i)
#         i -= 1
#     return n & 1
#
# LOOKUP_TABLE = [computeParity(i,8) for i in range(2**16)]
#
# def parity(x : int) -> int :
#     x ^= x >> 32
#     x ^= x >> 16
#     return LOOKUP_TABLE[x & (2**16-1)]

if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
