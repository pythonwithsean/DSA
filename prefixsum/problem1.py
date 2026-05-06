import string

def init(S,d):
    N = len(S)
    k = set(S)
    for char in string.ascii_lowercase:
        temp = [0] * (N + 1)
        for i in range(N):
            if S[i] == char:
                temp[i + 1] = 1
        for i in range(N):
            temp[i + 1] += temp[i]
        if char in k:
            d[ord(char) % 26] = temp
def getMostCommon(S,L,R):
    D =  [0] * 26
    init(S,D)
    K = set(S)
    res = ['a',0]
    for char in string.ascii_lowercase:
        if char not in K:
            continue
        freq = D[ord(char) % 26][R + 1] - D[ord(char) % 26][L]
        if freq > res[1]:
            res[0] = char
            res[1] = freq
    print(res[0])
    return res[0]
getMostCommon("aababbaaabbcc",0,3) #
