from test_framework import generic_test


def gcd(x: int, y: int) -> int:
    return x if y==0 else gcd(y,x%y)

# redo problem (without recursive stack)
def gcd(x: int, y: int) -> int:
    while (x >0) :
        y,x = x, y%x
    return y


if __name__ == '__main__':
    exit(generic_test.generic_test_main('euclidean_gcd.py', 'gcd.tsv', gcd))
