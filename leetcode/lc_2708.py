from typing import List
import math

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        """
            - You are given a 0 indexed integer array nums
            - representing the score of the students in an exam
            - group of students with the maximal strength (none empty)
            - Where the strength of a group of students is nums[i] * ... nums[ik]
            return the maximum strength of a geroup the teacher can creater
            1 <= nums_length <= 13
            nums[i]


        dp[i] -> storing the max strength

        [-4] -> -4

        [-4,-5,-4]

        -4 -> skip
        -4 * -5 go with it


        [0] -> curr

        take it or leave it

        [1] -> return num

        [-4,-5,-4]


        take it or leave

        -4 * -5 = 20 * -4
                - 20

        """

        N = len(nums)
        memo = {}
        def dp(i,amount):
            if i == N:
                return amount
            # take
            if (i,amount) in memo:
                return memo[(i,amount)]
            if amount == -math.inf:
                # start as me as the current amount
                take = dp(i+1,nums[i])
                # start with the origina -math.inf
                skip = dp(i+1,amount)
            else:
                # start next with me * amount
                take = dp(i +1,nums[i] * amount)
                # start next without me just the amount
                skip = dp(i + 1, amount)
            res = max(take,skip)
            memo[(i,amount)] = res
            return res
        res = dp(0,-math.inf)
        return res

"""
    This was a take it or leave it problem that required
    2 states the current position and the amount i had at each position
    at each position i needed to make sure i check if the amount i had was the default
    if it was i needed to handle that correctly
"""
