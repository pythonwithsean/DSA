
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
m = 0

# for i in range(len(nums)):
# sum = n]
# 	for j in range(i , len(nums)):
# 		sum += nums[j] 
# 		m = max(m,sum)

curr_sum = 0
start = 0 

for end in range(len(nums)):
	curr_sum += nums[end]
	
	m = max(curr_sum, m)

	if curr_sum < 0:
		curr_sum = 0
		start = end + 1


print(m)

