class NumArray:

    def __init__(self, nums):
        self.nums = nums 
       
    def sumRange(self, left, right):
        while left < right: 
            next = left + 1 
            self.nums[next] += self.nums[left]
            left += 1
        return self.nums[right]



num = [-2, 0, 3, -5, 2, -1]
obj = NumArray(num)
print(obj.sumRange(2,5))
