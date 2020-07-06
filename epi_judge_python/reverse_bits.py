from test_framework import generic_test


def reverse_bits_pdac(x: int) -> int:
    x = (x & 0xFFFFFFFF00000000) >> 32 | (x & 0x00000000FFFFFFFF) << 32
    x = (x & 0xFFFF0000FFFF0000) >> 16 | (x & 0x0000FFFF0000FFFF) << 16
    x = (x & 0xFF00FF00FF00FF00) >> 8  | (x & 0x00FF00FF00FF00FF) << 8
    x = (x & 0xF0F0F0F0F0F0F0F0) >> 4  | (x & 0x0F0F0F0F0F0F0F0F) << 4
    x = (x & 0xCCCCCCCCCCCCCCCC) >> 2  | (x & 0x3333333333333333) << 2
    x = (x & 0xAAAAAAAAAAAAAAAA) >> 1  | (x & 0x5555555555555555) << 1
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits_pdac))
