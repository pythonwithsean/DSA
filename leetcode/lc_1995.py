from typing import List

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:



        """

            a + b + c  == d

            nums[a] + nums[b] + nums[c] == nums[d]
            nums[a] + nums[b] == nums[d] - nums[c]

            [3,3,6,4,5]


        """
        N = len(nums)
        res = 0
        for i in range(N):
            for j in range(i+1,N):
                for k in range(j+1,N):
                    for l in range(k+1,N):
                        if nums[i] + nums[j] + nums[k] == nums[l]:
                            res += 1
        return res
