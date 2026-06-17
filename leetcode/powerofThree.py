n = 27
l = 0
r = n
found = False
while l < r:
  mid = l + (r + l) // 2
  if 3 ** mid ==  n:
    found = True
    print(mid)
    break
  elif 3 ** mid < n:
   l = mid
  else:
			r = mid 
   
print(found)


