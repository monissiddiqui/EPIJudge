from typing import List, Callable

from test_framework import generic_test

# """
# Solution 1 using recursion and splitting sub arrays. selecting the optimal buy points among
# the right and left subarrays and the min of the left subarray with the max of the right.
# """
# def buy_and_sell_stock_once(prices: List[float]) -> float:
#     buy, sell, imin, imax = get_buy_sell_points_add_aggregates(prices, 0, len(prices))
#     if buy is not None and sell is not None:
#         return prices[sell] - prices[buy]
#     return 0.0
#
# """
# checks the subarray defined by prices[start:end + 1] and returns the optimal buy sell point
# along with the value that beats out the other values in the array specified by the compare function
# """
# def get_buy_sell_points_add_aggregates(prices : List[float], start, end : int ) -> (int, int, int, int) :
# # def get_buy_sell_points_add_aggregates(prices, start, end):
#     # base cases
#     if start == end: return None, None, None, None
#     if end - start == 1: return None, None, start, start
#     if end - start == 2:
#         i1, i2 = start, end - 1
#         if prices[i1] < prices[i2]:
#             return i1, i2, i1, i2
#         else:
#             return None, None, i2, i1
#
#     # recursive case when splitting the array
#     resultStart, resultEnd = start, end - 1
#     resultMin, resultMax = 0,0
#     middle = (end + start) // 2
#     s1, e1, min1, max1 = get_buy_sell_points_add_aggregates(prices, start, middle)
#     s2, e2, min2, max2 = get_buy_sell_points_add_aggregates(prices, middle, end)
#
#     if min1 is not None:
#         resultMin = min1
#     elif min2 is not None:
#         resultMin = min2
#     if min1 is not None and min2 is not None:
#         resultMin = min1 if prices[min1] < prices[min2] else min2
#
#     if max1 is not None:
#         resultMax = max1
#     elif max2 is not None:
#         resultMax = max2
#     if max1 is not None and max2 is not None:
#         resultMax = max1 if prices[max1] > prices[max2] else max2
#
#     # compare left and right optimal buy points
#     # compare left min and right max buy points
#
#     maxSell = 0
#     if s1 is not None and e1 is not None:
#         maxSell = prices[e1] - prices[s1]
#         resultStart, resultEnd = s1, e1
#     if s2 is not None and e2 is not None and prices[e2] - prices[s2] > maxSell:
#         maxSell = prices[e2] - prices[s2]
#         resultStart, resultEnd = s2, e2
#     if max2 is not None and min1 is not None and prices[max2] - prices[min1] > maxSell:
#         resultStart, resultEnd = min1, max2
#
#     return resultStart, resultEnd, resultMin, resultMax

# # Solution 2 using the sliding window technique.
# """
# expand the sliding window's right side to find the sell time and contract the left side to
# find the best buy time.
# """
# def buy_and_sell_stock_once(prices: List[float]) -> float:
#
#     # find the index for the minimum among all values through to the current index
#     minUpTo = [0] * len(prices)
#     for i in range(1,len(prices),1) :
#         minUpTo[i] = i if prices[i] < prices[minUpTo[i-1]] else minUpTo[i-1]
#
#     # then find the index for the maximums among all values from the index through the rest of the array
#     currMax = -1
#     buy, sell = minUpTo[currMax], currMax
#     for i in range(len(prices)-1,0,-1) :
#         if prices[i] > prices[currMax] :
#             currMax = i
#         if (prices[currMax] - prices[minUpTo[i]]) > (prices[sell] - prices[buy]) :
#             buy = minUpTo[i]
#             sell = currMax
#
#     profit = prices[sell] - prices[buy]
#     return profit if profit > 0 else 0


"""
SOLUTION 3, found in the book. This is a better way than doing the second solution above, as it solves in one pass
and uses O(1) space. It doesn't need to store the mininum seen up to values array.
"""
# def buy_and_sell_stock_once(prices: List[float]) -> float:
#     minSoFar = prices[0]
#     maxProfit = 0
#     for p in prices:
#         maxProfit = max(p - minSoFar,maxProfit)
#         minSoFar = min(p,minSoFar)
#     return maxProfit

# Redo problem
def buy_and_sell_stock_once(prices: List[float]) -> float:
    minSoFar = float("inf")
    maxProfit = 0
    for p in prices :
        maxProfit = max(maxProfit,p - minSoFar)
        minSoFar = min(minSoFar,p)
    return maxProfit

# This is the way I solved the problem in leetcode. It is slightly more complicated but still
# optimal. Basically keep extending the window to sell
def buy_and_sell_stock_once_differential_method(prices: List[float]) -> float:
    currProfit = 0
    maxProfit = 0
    for i in range(1,len(prices)) :
        diff = prices[i] - prices[i-1]
        currProfit = max(currProfit + prices[i] - prices[i-1],0)
        maxProfit = max(currProfit,maxProfit)
    return maxProfit



if __name__ == '__main__':

    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once_differential_method))
