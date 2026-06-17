score = [10,3,8,9,4]
res = score.copy()
s = sum(score)

# We Get the Biggest
for i in range(len(score)):
  score[i] = s - score[i]
score.sort()
for j in range(len(score)):
  val = s - res[j]
  position = score.index(val) + 1
  if position == 1:
    res[j] = "Gold Medal"
  elif position == 2:
    res[j] = "Silver Medal"
  elif position == 3:
    res[j] = "Bronze Medal"
  else: 
      res[j] = str(position)
      
print(res)