from collections import Counter
def hammingWeight(n): 	
  print(Counter()["1"])

def toBin(n):
  remStr = ""
  val = n // 2
  rem = n % 2
  remStr += str(rem)
  while val > 0:
    rem = val % 2
    val = val // 2
    remStr += str(rem)
  return remStr[::-1]
 
print(toBin(11))