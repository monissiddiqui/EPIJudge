from typing import List

from test_framework import generic_test

from collections import deque

# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    isPrime = [True] * (n+1)
    primes = deque([], maxlen=n)
    for i in range(2,n+1) :
        if isPrime[i] :
            primes.append(i)
            j = 2 *i
            while j <= n :
                isPrime[j] = False
                j += i
    return list(primes)



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
