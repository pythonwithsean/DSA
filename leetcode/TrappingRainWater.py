height = [0,1,0,2,1,0,1,3,2,1,2,1]
maxLeft = [0] * len(height)
maxRight = [0] * len(height)
minArr = [0] * len(height)
maxRight[-1] = 0 
maxLeft[0] = 0
maxR = 0
maxL = 0
for i in range (1,len(height)):
    maxL = max(maxL, height[i - 1])
    maxLeft[i] = maxL

for i in range (len(height)-2, -1, -1):
    maxR = max(maxR, height[i + 1])
    maxRight[i] = maxR


for i in range(len(minArr)):
    val = min(maxLeft[i], maxRight[i])
    if val <= 0:
        minArr[0] = 0
    else:
        minArr[i] = val


print(maxLeft)
print(maxRight)
print(minArr)
for i in range(len(minArr)):
    v = height[i] - minArr[i]
    if v <= 0:
        minArr[0] = 0
    else:
        minArr[i] = v

print(minArr)
