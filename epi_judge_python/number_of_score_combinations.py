from typing import List

from test_framework import generic_test


# def num_combinations_for_final_score_optimized_space(final_score: int,
#                                      individual_play_scores: List[int]) -> int:
#
#     Combs = [0] * (final_score+1)
#     Combs[0] = 1
#     for points in individual_play_scores :
#         for score in range(final_score - points +1) :
#             if score + points <= final_score :
#                 Combs[score + points] += Combs[score]
#     return Combs[final_score]
#
# def num_combinations_for_final_score(final_score: int,
#                                      individual_play_scores: List[int]) -> int:
#     t = [[0]*(final_score+1)]* len(individual_play_scores)
#     t[0] = [1 if i %individual_play_scores[0] == 0
#             else 0 for i in range(final_score+1)]
#     for i in range(len(individual_play_scores)) :
#         t[i][0] = 1
#     for i in range(1,len(individual_play_scores)) :
#         for w in range(1, final_score +1) :
#             t[i][w] = t[i-1][w]
#             if w >= individual_play_scores[i] :
#                 t[i][w] += t[i][w-individual_play_scores[i]]
#     return t[-1][-1]

'''
Redo Problem.
'''
def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    t = [0] * (final_score +1)
    t[0] = 1
    for s in individual_play_scores :
        for w in range(final_score+1) :
            if s <= w :
                t[w] += t[w-s]
    return t[-1]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
