s = "(){}[]"

d = {
	"{": "}",
 "(": ")",
 "[": "]"
}

stack = []
for i in range(len(s)):
  if s[i] == "[":
    stack.append("[")
  elif s[i] == "{":
    stack.append("{")
  elif s[i] == "(":
    stack.append("(")
  else: 
    elm = stack.pop()
    if s[i] == d[elm]:
      pass
    else:
      print("Invalid") 
  
if not stack:
  print("Valid")
else:
  print("Invalid")
      
      
