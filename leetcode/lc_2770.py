from typing import List

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:

        """
            You are given a 0 indexed array nums of n integers
            and an integer target

            you are initally positioned at index 0
            in one step you can jump from index i to any index
            such taht

            0 <= i < j < n
            -target <= nums[j] - nums[i] <= target

            return the max number of jumps you can make to reach n-1

            if there is no way return -1

            choices

            - you can jump to inany index such taht j > i

            - and nums[j] - nums[i] <= target


            1,2,5,6,7,8,10

            dp(pos) -> represent something

            dp[0] -> max number of jumps


            state -> complete configuration of the world

            light -> on,off

            fib(n)

            1,1


            sean_in_room,light_on
            1,1
            1,0
            0,1
            0,0


            fib(n) -> fib(n-1) + fib(n-2)

        """

        N = len(nums)
        memo = [None] * N
        def dp(pos):
            if pos == N-1:
                return 0
            if memo[pos] != None:
                return memo[pos]
            best = -1
            for j in range(pos+1,N):
                if abs(nums[j] - nums[pos]) <= target:
                    res = dp(j)
                    if res != -1:
                        best = max(1 + res,best)
            memo[pos] = best
            return best

        return dp(0)
