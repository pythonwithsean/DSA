nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
m = nums[0]
curr_sum = nums[0]

for i in range(1,len(nums)):
	
	curr_sum = max(int(nums[i]),int( curr_sum + nums[i]))
	m = max(curr_sum, m)

print(m)

