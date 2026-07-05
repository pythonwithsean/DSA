from typing import List
from functools import cache
import math

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:


        """
            You are given a square board of chars

            You are start at the bottom right square marked S

            you need to reach the top left marked with E

            you can go up,left,up-left

            return 2 integers

            - the max sum of numeric characters
            - the number of paths that you can take to get that max sum
            taken modulo 10^9 + 7
            if no path return [0,0]

            ["E23",
             "2X2",
             "12S"]

            2 + 3 + 2 = 7
            2 + 1 + 2 = 5


           ["E12",
            "1X1",
            "21S"]

            1 + 2 + 1 = 4
            1 + 2 + 1 = 4

            [4,2]


           ["E11",
           "XXX",
           "11S"]


        """

        MOD = 10**9 + 7
        N = len(board)
        @cache
        def dp(i,j):
            if not (0 <= i < N and 0 <= j <= N):
                return [-math.inf ,0]
            if board[i][j] == "X":
                return [-math.inf,0]
            if board[i][j] == "E":
                return [0,1]

            curr_ways = 0
            c = 0 if board[i][j] == "S" else int(board[i][j])

            upc,upways = dp(i-1,j)
            leftc,leftways= dp(i,j-1)
            upleftc, upleftways = dp(i-1,j-1)

            m = max(upc,leftc,upleftc)

            if m == -math.inf:
                return [-math.inf,0]

            if upc == m:
                curr_ways += upways
            if leftc == m:
                curr_ways += leftways
            if upleftc == m:
                curr_ways += upleftways

            return [c + m % MOD ,curr_ways % MOD]

        res = dp(N-1,N-1)
        if res[0] == -math.inf:
            return [0,0]
        return res
