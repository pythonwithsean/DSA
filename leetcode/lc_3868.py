from collections import Counter

class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        """
            You are given two integer arrays nums1 and nums2 of size n
            You can perform the following two operatins any number of times

            We can swap elements between the same array for free
            But to swap elements between arrays costs 1

            The goal is to make nums1 and num2 identical


            N = 10000

            [10,20], [20,10]
            [10,20]    [10,20] costs 0


            [10,10], [20,20]

            2
            if any number appears once then it is not possible for both arrays to be identical
            All numbers must not appear once
            number count must be even

            10: 2
            20: 2


            [10,20,20], [10]



            question now becomes how many swaps do we need to do between nums1 and nums2

        """

        c = Counter(nums1 + nums2)
        if c1 == c2:
            return 0

        c1 = Counter(nums1)
        c2 = Counter(nums2)

        # can be divided
        for count in c.values():
            if count % 2 != 0:
                return -1

        # all the numbers in one part
        if len(c1) == 1 and len(c2) == 1:
            return len(nums1) // 2

        # it is possible
        res = 0

        for num, count in c1.items():
            total = c[num]
            should_have = total // 2
            if count > should_have:
                res += count - should_have
        return res


"""
        Key observation:
        - Swaps within the same array are free.
        - Therefore, positions do not matter.
        - The problem reduces to balancing the frequency of each value
          between nums1 and nums2.

        For the arrays to become identical, each value must appear the
        same number of times in both arrays.

        If a value appears T times overall, then each array must end up
        with T // 2 copies of that value.

        Thus:
        1. Every total frequency must be even, otherwise splitting the
           value evenly between both arrays is impossible.
        2. For every value that appears too many times in nums1, the
           excess copies must be moved to nums2.
        3. The total excess in nums1 equals the total deficit in nums1,
           so counting the excess gives the minimum number of required
           cross-array swaps.
"""
