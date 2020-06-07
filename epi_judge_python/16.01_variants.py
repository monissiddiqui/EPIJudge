from typing import List

from test_framework import generic_test

'''
VARIANT 1 
Solve the same problem using O(s) space.

VARIANT 2
Write a program that takes a final score and scores for individual plays, 
and returns the number of sequences of plays that result in the final score.
For example, 18 sequences of plays yield a score of 12. Some examples are 
(2,2,2,3,3), <2,3,2,2,3>, <2,3,7), <7,3,2>.

VARIANT 3 
Suppose the final score is given in the form (s,s'), i.e., Team L scored s 
points and Team 2 scored s' points. How would you compute the number of 
distinct scoring sequences which result in this score? For example, if the
final score is (6,3) then Team 1 scores 3, Team 2 scores 3, Team L scores 3
is a scoring sequence which results in this score.

VARIANT 4
Suppose the final score is (s,s'). How would you compute the maximum number 
of times the team that lead could have changed? For example, if s = 10 and 
s' = 6, the lead could have changed 4 times: Team 1 scores 2, then Team 2 
scores 3 (lead change), then Team L scores 2 (lead change), then Team 2 
scores 3 (lead change), then Team 1 scores 3 (lead change) followed by 3.

VARIANT 5
You are climbing stairs. You can advance 1 to k steps at a time. 
Your destination is exactly n steps up. Write a program which takes as 
inputs n atrtdk and returns the number of ways in which you can get to your 
destination. 

For example, rt n = 4 andk = 2, there are five ways in which to get to the 
destination:
o four single stair advances,
o two single stair advances followed by a double stair advance,
o a single stair advance followed by a double stair advance followed by a single stair advance, o a double stair advance followed by two single stairs advances, and
o two double stair advances.

'''


# VARIANT 1
def num_combinations_for_final_score_optimized_space(final_score: int,
                                                     individual_play_scores: List[int]) -> int:
    Combs = [0] * (final_score+1)
    Combs[0] = 1
    for points in individual_play_scores :
        for score in range(final_score - points +1) :
            if score + points <= final_score :
                Combs[score + points] += Combs[score]
    return Combs[final_score]

'''
VARIANT 2
since we now care about the order in which the points occur, the 
different points can be interleaved among eachother. 

THis is similar to variant 1, except the outer loop is now the 
total score and the inner loop is through the individual scores.
What is done here is take a current total score and then take its
possible number of sequences and add it to the possible sequences for
the current total score + any of the individual scores. This forard propogat
'''
def num_sequences_for_final_score(final_score: int,
                                                     individual_play_scores: List[int]) -> int:
    Combs = [0] * (final_score+1)
    Combs[0] = 1
    for score in range(final_score - min(individual_play_scores) +1) :
        for points in individual_play_scores :
            if score + points <= final_score :
                Combs[score + points] += Combs[score]
    return Combs[final_score]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
