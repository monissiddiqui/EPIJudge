from test_framework import generic_test


def roman_to_integer(s: str) -> int:
    res = 0
    numeral = {"I" : {"value": 1, "priority": 0},
                  "V" : {"value": 5, "priority": 1},
                  "X" : {"value": 10, "priority": 2},
                  "L" : {"value": 50, "priority": 3},
                  "C" : {"value": 100, "priority": 4},
                  "D" : {"value": 500, "priority": 5},
                  "M" : {"value": 1000, "priority": 6}
                  }
    i = 0
    prev = "M"
    while i < len(s) :
        res += numeral[s[i]]["value"]
        if numeral[prev]["priority"] < numeral[s[i]]["priority"] :
            res -= 2*numeral[prev]["value"]
        prev = s[i]
        i += 1
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('roman_to_integer.py',
                                       'roman_to_integer.tsv',
                                       roman_to_integer))
