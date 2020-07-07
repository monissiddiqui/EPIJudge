from test_framework import generic_test

from collections import deque

def look_and_say(n: int) -> str:
    num = ["1"]
    for _ in range(n-1) :
        newNum = deque([],maxlen=2*len(num))
        count = 1
        prev = num[0]
        for i in range(1,len(num)) :
            if num[i] == prev :
                count += 1
            else :
                newNum.append(str(count))
                newNum.append(prev)
                prev = num[i]
                count = 1
        newNum.append(str(count))
        newNum.append(prev)
        num = list(newNum)

    return ''.join(num)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
