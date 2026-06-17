s = ["h","e","l","l","o"]
r = len(s) - 1
l = r - 1 
curr = r + 1
while l >= 0:
  elem = s[l]
  s.insert(curr, elem)
  l  -= 1
  curr += 1
print(s)
for i in range(r -1 , -1, -1):
  s.pop(i)
  
  
print(s)
	