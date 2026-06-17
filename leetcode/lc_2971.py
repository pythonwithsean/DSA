import math

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        """
            You are given positive numbers of length n

            A polygon is a closed plan figure that has atleast 3 sides

            The longest side of a polygon is smaller than the sum of the other side

            a + b > c that makes a polygon

            The perimiter of a polygon is the sum of the lengths of its sides


            5 + 5 > 5 so the the perimiter is 15

            1,12,1,2,5,3 -> 1 + 1 + 2 + 3 + 5

            1 2 4
            1,1,2,3,5,12

        """
        N = len(nums)
        best = -math.inf
        nums.sort()
        prev = sum(nums[:2])
        for i in range(2,N):
            if prev > nums[i]:
                best = prev + nums[i]
            prev += nums[i]

        return best if best != -math.inf else -1



"""
    Intution


    The problem is asking for the biggest polygon

    a polygon has at least 3 sides

    lets say the amount of sides a polygon has is k

    then that means the sum of all the numbers from sum([0:k]) > nums[k]
    if that is the case then we have found found a perimiter so then we record that and keep moving on



"""
