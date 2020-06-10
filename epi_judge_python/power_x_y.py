from test_framework import generic_test

'''
The number Y has a binary representation, so we can shorten the number of operations to computing the 
powers for the bits that are set in Y and add them in the exponent of x.

so an addditional data structure holding the multiples of the powers of x and then
a loop to extract the last set bit in Y and find it in the lookup table
'''
def power(x: float, y: int) -> float:
    n = 1
    prod = x
    LSB = y & ~(y-1)
    res = 1
    invert = y < 0
    y = abs(y)
    while n <= y :
        if n == LSB :
            res *= prod
            y &= y-1
            LSB = y & ~(y-1)
        n <<= 1
        prod *= prod

    return res if not invert else 1/res


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
