from test_framework import generic_test

from collections import deque

'time complexity is first step iterates over here '
def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    mapCharToNum = {}
    mapNumToChar = {}
    for i,c in enumerate("0123456789ABCDEF") :
        mapNumToChar[i] = c
        mapCharToNum[c] = i

    num = 0
    sign = ""
    if num_as_string[0] == "-" :
        sign = "-"
    for c in num_as_string :
        if c in mapCharToNum :
            num *= b1
            num += mapCharToNum[c]
    sb = deque(maxlen=64)
    while num > 0:
        sb.appendleft(mapNumToChar[num % b2])
        num //= b2
    sb.appendleft(sign)
    b2_string = ''.join(sb)
    return b2_string if b2_string else "0"




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
