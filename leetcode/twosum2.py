nums, target = [2, 3, 4], 6
d = {}

for i in range(len(nums)):
    val = target - nums[i]  # the value needed to reach the target
    if val in d:
        return [d[val] + 1, i + 1]  # print indices in a 1-based index
    d[nums[i]] = i
