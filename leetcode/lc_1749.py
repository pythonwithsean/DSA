from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        """
            You are given an integer arr nums. The absolute sum of a subarray nums[l] ..... nums[r] is the abs sum of the nums

            return the max absolute sum of any possibly empty subarray of nums

            Note that abs(x) is defined
            if x is negative abs(x) = -x
            else abs(x) = x

            goal:
                find the max absolute sum of any subarray including empty ones

            kadanes algorithm

            one approach
            brute force O(N^2) -> every possibility


            [1,-3,2,3,-4]

             1

            [2,-5,1,-4,3,-2]
             ^    ^

            skip

            [1,-3,2,3]
             1  2 4 7

            [1,3,2,3,4]

             prefix sum ???
             dp ???

             with dp
             what state is important

             [2,-5,1,-4,3,-2] -> we want the max abs subarray sum


             - meaning numbers withiun the sum keep their sign but the final prodcut needs to be updated

             we want to either include numbers or exclude numbers but excluding will mean that we are starting a brand new subarray

             try
             with prev + us
             or just us


            brute force - does not work
            kadane - does not work - greedy
            dp -> dp

            [2,-5,1,-4,3,-2]

            pos

            subsequences
            subarray

            take -> take curr -> go to the next position
            skip -> start on next position -> creating


            find the max positive sum of subarray in an array

            find the max negative sum of subarry in an array


        """

        curr = nums[0]
        curr_min = nums[0]
        res = nums[0]
        min_res = nums[0]
        for num in nums[1:]:
            # max kadane
            curr = max(num,curr + num)
            res = max(res,curr)
            # min kadane
            curr_min = min(num, curr_min + num)
            min_res = min(min_res,curr_min)

        res = max(res,curr)
        min_res = min(min_res,curr_min)
        return max(res,abs(min_res))



"""
    Really interesting problem this was a very strong kadane algorithm solution and how it works
    is we need to understand what kadanes algorithm does

    It allows us to be able get the max positive sum of a subarray with positive and negative numbers why
    because at each step we choose the best choice do we continue our sum or throw everything away and start a brand new subarray

    So what happens when we take the reverse we can be at the extreme positive end or i can be at the negative left end
    and if we do the abs() of it we can pick the max of both of them

    min_res gonna be the kadane of the opposite side max_res allow us to find the max of the positive side and min kadane allows for max of the positive side

    min                                        max
    <-------------------------------------------->

    with max kadane i can i can access the max with min kadane im on the other end

"""
