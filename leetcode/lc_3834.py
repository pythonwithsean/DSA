class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:

        stack = []
        N = len(nums)
        """
            [2,1,1,2]

            [2,2]


        """

        for i in range(N):
            if not stack:
                stack.append(nums[i])
                continue
            stack.append(nums[i])
            while len(stack) > 1 and stack[-1] == stack[-2]:
                stack.append(stack.pop() + stack.pop())
        return stack
