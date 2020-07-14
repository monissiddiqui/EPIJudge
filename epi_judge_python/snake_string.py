from test_framework import generic_test

from itertools import cycle

def snake_string_pretty_print(s: str) -> str:
    direction = cycle([-1,-1,1,1])
    position = 2
    layers = [[" "]*len(s) for _ in range(3)]
    for i in range(len(s)) :
        position += next(direction)
        layers[position][i] = s[i]
    return '\n'.join([' '.join(layer) for layer in layers])

def snake_string(s: str) -> str:
    res = [""] * len(s)
    i = 0
    for j in range(1,len(s),4) :
        res[i] = s[j]
        i += 1
    for j in range(0,len(s),2) :
        res[i] = s[j]
        i += 1
    for j in range(3,len(s),4) :
        res[i] = s[j]
        i += 1
    return ''.join(res)

if __name__ == '__main__':
    print("Hello World!")
    print(snake_string("Hello World!"))
    exit(
        generic_test.generic_test_main('snake_string.py', 'snake_string.tsv',
                                       snake_string))
