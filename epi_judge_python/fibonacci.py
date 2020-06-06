from test_framework import generic_test


def fibonacci(n: int) -> int:
    if n<= 1 : return n
    f0,f1 = 0,1
    for i in range(1,n) :
        f0,f1 = f1, f0 + f1
    return f1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('fibonacci.py', 'fibonacci.tsv',
                                       fibonacci))
