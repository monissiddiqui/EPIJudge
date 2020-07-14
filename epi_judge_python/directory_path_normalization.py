from test_framework import generic_test

from collections import deque

def shortest_equivalent_path(path: str) -> str:
    path = path.split('/')
    stack = deque([],maxlen=len(path))
    i = 0
    root = ""
    if path[0] == "" :
        i += 1
        root = "/"

    nothing = set(["","."])
    for p in path[i:] :
        if p == ".." and stack and p != stack[-1]:
            stack.pop()
        elif p not in nothing :
            stack.append(p)
    return root + '/'.join(stack)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
