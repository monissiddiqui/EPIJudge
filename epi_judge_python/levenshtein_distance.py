from test_framework import generic_test

'''
to change the word "Saturday" to "Sunday", note that the letter composition 
must match entirely, so the counts of the letters up to a certain index 
must be the same for each word.
i,j are index for Saturday and Sunday respectively. 

The LD can be calculated from subwords of the current words that are being compared.
If A[0] == B[0] then t[0][0] = 0  since no edits need to be made to the first character.

Given 0<i<len(A) and 0 <j<len(B), then t[i][0] = t[0][0] + i since i deletions would be 
needed to go form A[:i+1] to B[0] requires i deletes. In a similar vein t[0][j] = t[0][0] + j
since A[0] requires j more insertions to reach B[:j+1] 

Those are the initial conditions. Now for t[i][j], trying to find the Levenshtein distance
from A[:i+1] to B[:j+1]

We can consider 4 operations to get to doing the final transformation to get from A[:i+1]
to B[:j+1]. 

if A[i] == B[j], then LD can be t[i-1][j-1] since the final letters of the subwrod's don't 
require any edits.

It can also be the case that After transforming A[:j] to B[:j+1] an exra insert is made to have 
the transformation of A[:j+1]
Similarly a deletion of B[j] can be made to get from the A[:j+1]->B[:j]

ALternatively a substitutino of the final letter A[i] and B[j] can be made in addition to the 
transformation A[:i]->B[:j]

'''
def levenshtein_distance(A: str, B: str) -> int:
    # empty string cases with pure deletions/insertions
    if len(A) == 0 or len(B) == 0:
        return max(len(A),len(B))

    nA = len(A)
    nB = len(B)

    t = [[0 for _ in range(nB+1)] for _ in range(nA+1)]
    if A[0] != B[0] :
        t[0][0] = 1
    for i in range(nA+1) :
        t[i][0] = i#t[0][0] + i
    for j in range(1,nB+1) :
        t[0][j] = j#t[0][j] + j
    for i in range(1,nA+1) :
        for j in range(1,nB+1) :
            ld = t[i-1][j-1]
            if A[i-1] != B[j-1] :
                ld += 1
            t[i][j] = min(ld,t[i-1][j]+1,t[i][j-1]+1)
    return t[-1][-1]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
