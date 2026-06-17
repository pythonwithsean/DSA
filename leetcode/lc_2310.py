import math

class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        """
            consider two integer

            num and k consider a set fo positve integers with the following properties
            the sum of the integers must be num and unit digit must end with k

            return -1 if no such set exists
        """
        memo = {}
        def dp(target):
            if target == 0:
                return 0
            if target in memo:
                return memo[target]
            best = math.inf
            for op in range(1, target+1):
                if op % 10 == k:
                    best = min(best, 1 + dp(target - op))
            memo[target] = best
            return best

        res = dp(num)
        return res if res != math.inf else -1

"""
    Unbounded Knapsack problem where we treat candidates that end with k
    as possible choices that could lead the best solutuion

"""
