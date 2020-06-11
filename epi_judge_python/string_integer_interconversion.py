from enum import Enum

from test_framework import generic_test
from test_framework.test_failure import TestFailure

from collections import deque

# def int_to_string(x: int) -> str:
#     if x == 0: return '0'
#     mapIntToString = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
#     digits = []
#     sign = ""
#     if x < 0:
#         x *= -1
#         sign += "-"
#     while x > 0:
#         digits.append(mapIntToString[x % 10])
#         x //= 10
#     digits.append(sign)
#     return "".join(reversed(digits))
#
#
# def string_to_int(s: str) -> int:
#     mapStringDigitToInt = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
#     sign = 1
#     lastDigitIndex = 0
#     if s[0] not in mapStringDigitToInt:
#         sign = -1 if s[0] == "-" else 1
#         lastDigitIndex += 1
#
#     number = 0
#     tensFactor = 1
#     for i in range(len(s) - 1, lastDigitIndex - 1, -1):
#         number += tensFactor * mapStringDigitToInt[s[i]]
#         tensFactor *= 10
#     number *= sign
#
#     return number

# redo Problems
def int_to_string(x: int) -> str:
    sb = deque()
    mapIntToString = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
    isNegative = False
    if x < 0:
        isNegative = True
        x = -x
    while x > 0 :
        sb.appendleft(mapIntToString[x%10])
        x //= 10
    if isNegative: sb.appendleft("-")
    return ''.join(sb) if sb else "0"

def string_to_int(s: str) -> int:
    number = 0
    chartoNum = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
    for i in range(len(s)) :
        if s[i] in chartoNum :
            number *= 10
            number += chartoNum[s[i]]
    if s[0] == "-" :
        number *= -1
    return number


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
