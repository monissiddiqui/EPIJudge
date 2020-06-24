from typing import Set
from typing import Dict
from typing import List

from test_framework import generic_test

from collections import defaultdict
from collections import deque
import string


'''
Tried this and it runs very slow. There must be a more optimal solution. 
'''
# def transform_string(D: Set[str], s: str, t: str) -> int:
#     V : List[str] = list(D) + [t,s]
#     G : Dict[int,Set[int]] = defaultdict(set)
#     # build graph in O(n^2*l) where n is the number of strings in the dictionary and
#     # l is the maximum length of a string in the dictionary.
#     for u in range(len(V)) :
#         for v in range(u+1,len(V)) :
#             if len(V[u]) != len(V[v]) :
#                 continue
#             diffsFound = 0
#             for i in range(len(V[v])) :
#                 if V[v][i] != V[u][i] :
#                     diffsFound += 1
#                     if diffsFound > 1 :
#                         break
#             if diffsFound == 1 :
#                 G[u].add(v)
#                 G[v].add(u)
#
#     # Perform BFS and find string
#     distance = 0
#     bfsq = [len(V)-1]
#     while bfsq :
#         newbfsq = deque(maxlen=len(G))
#         for u in bfsq : # DEBUG change this to a list
#             if u == len(V) - 2 :
#                 return distance
#             for v in G[u] :
#                 if u != v and G[v] :
#                     newbfsq.append(v)
#             del G[u]
#         bfsq = list(newbfsq)
#         distance += 1
#     return -1

'''
This is slightly faster than the previous solution but still slow
'''
# def transform_string(D: Set[str], s: str, t: str) -> int:
#     bfsq = [s]
#     distance = -1
#     while bfsq :
#         newq = deque([],maxlen=len(D))
#         distance += 1
#         for w in bfsq :
#             if w == t :
#                 return distance
#             for v in list(D) :
#                 if len(v) != len(w) :
#                     D.discard(v)
#                     continue
#                 diffsFound = 0
#                 for i in range(len(w)) :
#                     if v[i] != w[i] :
#                         diffsFound += 1
#                     if diffsFound > 1 :
#                         break
#                 if diffsFound == 1 :
#                     D.discard(v)
#                     newq.append(v)
#         bfsq = list(newq)
#     return -1

'''
When visiting a node, instead of checking the remaining nodes in the dictionary to see if they
are one distance away from the current node, the node's possible variations can be checked to see
if they are in the dictionary.

For a given node, checking the remaining nodes would be O(d * l) where d is the number of nodes
in the dictionary. If checking the possible variations on the node, there are 26l possible variations
of the word that are one-distance away and checking to see if they are in the dictionary is O(1).
Creating the candidate string however costs O(l) time so if 26 * l is less than d, then it would be
better to check through the possible variations instead of checking the remaining dictionary items

'''
def transform_string(D: Set[str], s: str, t: str) -> int:
    if len(s) != len(t): return -1
    distance = -1
    bfsq = [s]
    D.discard(s)
    while bfsq :
        newq = deque([],maxlen=len(D))
        distance += 1
        for u in bfsq :
            if not D :
                break
            if len(u) != len(s):
                continue
            if u == t :
                return distance
            for i in range(len(u)) :
                for c in string.ascii_lowercase :
                    v = u[:i] + c + u[i+1:]
                    if v in D :
                        D.discard(v)
                        newq.append(v)
        bfsq = list(newq)
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_transformability.py',
                                       'string_transformability.tsv',
                                       transform_string))
