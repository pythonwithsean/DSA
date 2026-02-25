import collections
arr = [1,2,3,4,5]
N = len(arr)
pref = [0] * (N + 1)
collections.Counter().most_common()
for i in range(N):
    pref[i + 1] += pref[i] + arr[i]
print(pref)
