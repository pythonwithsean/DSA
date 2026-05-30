import heapq
from typing import List

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        """
            You are given an array nums of positive numbers

            in one operation you can choose any number from nums and reduce it to exactly half the number (note that you may choose this reduced number in the future operations)

            return the minimum number of operations to reduce the sum of nums by atleast half

            at least means greater -> >=

            [5,19,8,1] -> sum is equal to 33

            half of 33 is 16


            [19,8,5,1] = 33
            [9.5,8,5,1] = 23.5
            [8,5,4.75,1] = 18.75


        """



        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        s = sum(nums)
        h = s / 2
        turns = 0
        while True:
            b = -heapq.heappop(max_heap)
            n = b / 2
            if s - b + n <= h:
                return turns + 1
            else:
                if n >= b:
                    return turns + 1
                s = s - b + n
                heapq.heappush(max_heap,-n)
            turns += 1
