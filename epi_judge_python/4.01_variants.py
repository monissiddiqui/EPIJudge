"""
# Page 27 of EPI.

Write expressions that use bitwise operators, equality checks, and Boolean operators to do the following in O(1) time.
o Right propagate the rightmost set bit in x, e.g., tums (01010000)2 to (01011111)2.
o Compute r mod a power of two, e.9., retums 13 for77 mod 64.
o Testif risapower of 2,i.e.,evaluatestotrue forx=1.,2,4,8,...,falseforallothervalues.
"""


def rightPropogate(x: int) -> int:
    return x | (x - 1) if x != 0 else x


def modPowerOfTwo(x, p: int) -> int:
    # assume that p is a power of two
    return x & (p - 1)


def isAPowerOfTwo(x : int) -> bool :
    # assume x is
    return not x & (x-1) if x != 0 else False


if __name__ == '__main__':
    print("Testing 4.01 Variants")
    print("Testing the rightmost set bit propagation")
    assert (rightPropogate(0B10) == 0b11)
    assert (rightPropogate(0b100110) == 0b100111)
    assert (rightPropogate(0b10110011) == 0b10110011)
    assert (rightPropogate(-10) == -9)
    assert (rightPropogate(-22) == -21)
    assert (rightPropogate(0B0) == 0b0)
    assert (rightPropogate(-1) == -1)

    print("Testing the mod of a power of two")
    assert (modPowerOfTwo(4, 4) == 0)
    assert (modPowerOfTwo(5, 4) == 1)
    assert (modPowerOfTwo(15, 4) == 3)
    assert (modPowerOfTwo(0,1) == 0)
    assert (modPowerOfTwo(-1,4) == 3)
    assert (modPowerOfTwo(-3,4) == 1)

    print("Testing if a number is a power of two")
    assert (isAPowerOfTwo(0) == False)
    assert (isAPowerOfTwo(1) == True)
    assert (isAPowerOfTwo(4) == True)
    assert (isAPowerOfTwo(46) == False)
    assert (isAPowerOfTwo(-1) == False)
    assert (isAPowerOfTwo(-5) == False)
