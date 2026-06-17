class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
            Given a circular array meaning the next element from the last is the first element

            return the next greater number for ever element in nums
            meaning the next element that bigger than me it has to be infront or behind

            The next greater number of a number x is the first greater number from traversing left to right which means you could search

            monotonic decreasing

            [(2,1),(1,2)]
            [1,2,1]
            [2,-1,-1]




            [1,2,3,4,3]
            [2,3,4,-1,4]
            [(4,3),(3,4)]

        """

        N = len(nums)
        res = [-1] * N
        if N == 1: # only one element
            return res
        stack = [(nums[0],0)]

        for i in range(1,N):
            while stack and nums[i] > stack[-1][0]:
                res[stack[-1][1]] = nums[i]
                stack.pop()
            stack.append((nums[i],i))


        for i in range(N):
            while stack and nums[i] > stack[-1][0]:
                res[stack[-1][1]] = nums[i]
                stack.pop()
        return res



"""
    Intuition for this problem the array has a random order and
    we want to find the next bigger number for each number

    The catch is that there is a cycle or the array is a cyclic meaning that at index N - 1 the next elemnt
    is 0

    Approach to solving this problem

    Maintain a monotonic decreasing stack and fill as much numbers with the next biggest on the right

    When you reach the end of the array you have 2 cases

    1) The stack is empty and you have filled out all number with their next greatest
    2) You have some numbers in that case they are going to be in decreasing manner from biggest to smallest
    so what you will have to do is go through all the numbers from the begining and fill each array with next biggest number on the right cause there is a cycle a good way to visualize this is imagine

    [5,4,3,2,1] a cycle will mean we have [5,4,3,2,1] -> [5,4,3,2,1,5,4,3,2,1] notice how we just have to go through the array again to find the next biggest number on the right at the end of the second loop you would have filled
    all the numbers indexes with the next biggest number on the right
"""
