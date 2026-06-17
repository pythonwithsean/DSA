arr = [1,3,5,7,9]

ascArr = arr.s
descArr = arr.sort(reverse=True)
minVal = ascArr[0]
maxVal = descArr[0]
for i in range(1,4):
        minVal += ascArr[i]
        maxVal += descArr[i] 
        
print("{0} {1}".format(minVal,maxVal))   