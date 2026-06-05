import math
from typing import List
class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        """
            You are climbing a staircase with n + 1 steps numbered from 0 to n

            You are also given a 1 indexed integer array costs of length n

            where costs[i] is the cost of the ith step

            from step i you can jump only to step i + 1, i + 2, i + 3. The cost of jumping from step i to step j is defined as

            to go from i to j -> cost[j] + (j - i)^2


            n = 4
            [1,2,3,4]


            n



        """

        costs = [0] + costs
        N = n
        memo = [math.inf] * N
        def dp(i):
            if i >= N:
                return costs[N]
            if memo[i] != math.inf:
                return memo[i]
            best = math.inf
            for nxt in range(1,4):
                next_pos = i + nxt
                c = (costs[i] + dp(next_pos)) + ((next_pos - i))**2
                best = min(c,best)
            memo[i] = best
            return best
        return dp(0)
