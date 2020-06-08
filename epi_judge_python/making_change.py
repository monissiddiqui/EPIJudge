from test_framework import generic_test


def change_making(cents: int) -> int:
    coins = [100, 50,25, 10, 5, 1]
    count = 0
    for coin in coins :
        count += cents //  coin
        cents %= coin
    return count


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('making_change.py', 'making_change.tsv',
                                       change_making))
