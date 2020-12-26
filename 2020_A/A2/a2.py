#https://www.geeksforgeeks.org/combinations-in-python-without-using-itertools/
#https://www.mathsisfun.com/combinatorics/combinations-permutations.html
#https://docs.python.org/3/library/itertools.html#itertools.product
# 1 how to find all permutations S1 + S2 + S3 = P - brute force

from typing import List
from collections import defaultdict


def solution_bf(N: int, K: int, P: int, stacks: List[List]):
    res = 0

    def product(set_len, n_sets):
        """ Iteratively generate all permutations with repetition."""
        res = [[]]
        for n in range(n_sets):
            new_res = []
            for x in res:
                for y in range(set_len + 1):
                    new_res.append(x + [y])
            res = new_res
        return res

    def product_recursive(set_len, n_sets):
        """Recursively generate all permutations with repetition."""
        if n_sets == 0:
            return [[]]
        res = []
        for y in range(set_len + 1):
            for x in product_recursive(set_len, n_sets - 1):
                res.append(x + [y])
        return res

    for p in product_recursive(K, N):
        if sum(p) == P:
            s = 0
            for i, np in enumerate(p):
                s += sum(stacks[i][:np])
            res = max(res, s)
    return res



def solution_mem(N: int, K: int, P: int, stacks: List[List]):
    """Memoization"""

    res = 0
    dp = defaultdict(lambda: defaultdict(int))
    def max_beauty(curr_stk, K, plates_left):
        if dp[curr_stk][plates_left]:
            return dp[curr_stk][plates_left]

        if plates_left <= 0 or curr_stk < 0:
            return 0

        max_b = max_beauty(curr_stk - 1, K, plates_left)
        curr_b = 0
        for i in range(min(plates_left, K)):
            curr_b += stacks[curr_stk][i]
            max_b = max(max_b, curr_b + max_beauty(curr_stk - 1, K, plates_left - i - 1))

        dp[curr_stk][plates_left] = max_b
        return max_b
        
    res = max_beauty(N - 1, K, P)
    return res


def solution(N: int, K: int, P: int, stacks: List[List]):
    """Dynamic Programming - intermediate state"""
    sums = [[0 for j in range(K + 1)] for i in range(N + 1)]
    dp = [[0 for j in range(P + 1)] for i in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, K + 1):
            sums[i][j] = stacks[i - 1][j - 1]
            sums[i][j] += sums[i][j - 1]

    for i in range(1, N + 1):
        for j in range(1, P + 1):
            for x in range(min(j + 1, K + 1)):
                dp[i][j] = max(dp[i][j], sums[i][x] + dp[i - 1][j - x])

    return dp[-1][-1]


tc = int(input())
for i in range(1, tc + 1):
    N, K, P = input().split()
    stacks = []
    for k in range(int(N)):
        stacks.append([int(p) for p in input().split()])
    out = solution(int(N), int(K), int(P), stacks)
    print("Case #{}: {}".format(i, out))