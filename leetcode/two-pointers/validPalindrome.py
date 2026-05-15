s ="race a car".lower().strip().replace(" ", "")
stack = []
for i in range(len(s) -1, -1, -1):
  if(s[i].isalnum()):
    stack.append(s[i])
res = []
print(stack)
s.strip()

for j in range(len(s)):
  if s[j].isalnum(): 
    res.append(s[j])
    charStack = stack.pop()
    if s[j] != charStack:
      print("False")
      break
print("True")
print(res)