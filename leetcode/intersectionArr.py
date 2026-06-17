nums1,nums2 = [1,2,2,1], [2,2]

d1 = {}
d2 = {}
res = []

for n in nums1:
  if d1.__contains__(n):
    d1[n] = d1.get(n) + 1
  else:
    d1.setdefault(n,1)   
      
for n in nums2:
  if d2.__contains__(n):
    d2[n] = d2.get(n) + 1
  else:
    d2.setdefault(n,1)
    
for val,count in d1.items():
  if d2.__contains__(val):
    minCount = min(d1.get(val), d2.get(val))
    for i in range(minCount):
      res.append(val)
    
print(res)