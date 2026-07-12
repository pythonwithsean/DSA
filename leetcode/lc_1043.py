from typing import List
import math

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        """
            Given an integer arr partition the array into
            contigious subarrays of length at most k
            after paritioning each, subarray has their values changed to
            become the maximum value of that subarray

            return th largest sum of the given array after paritioning

            at most means max k

            if k = 1 then the result is just sum(arr)

            [1,15,7,9,5,10] k = 3

            [1] [15] [7] [9] [5] [10]

            [1,15,7], [9], [10,10]

            1 <= arr.length <= 500

            [6] -> 6
            [6,12] -> 24



        """
        # pref = []
        # for num in arr:
        #     if not pref:
        #         pref.append(num)
        #         continue
        #     pref.append(max(pref[-1], num))
        # print(pref)

        # we could be within
        # we could be going too much

        N = len(arr)
        memo = [-math.inf] * N
        def dp(pos):
            if pos >= N:
                return 0
            if memo[pos] != -math.inf:
                return memo[pos]
            # base case
            best = -math.inf
            curr_max = 0
            for i in range(pos,N):
                # calculate max as you go along
                curr_max = max(curr_max, arr[i])
                size = (i - pos) + 1
                if size > k:
                    break
                else:
                    best = max(best, (curr_max * size) + dp(pos+size))
            memo[pos] = best
            return best
        return dp(0)
