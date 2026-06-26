import math
MOD = (10**9 + 7)


"""
    n = 10

    10
    -1

    100

    90
                    10


            0/1 = 0
"""


def solution(n):
    count = 0

    while n > 9:
        s = str(n)
        d = int(s[0])
        rest = s[1:] if len(s) > 1 else "0"
        tail = int(rest)
        factor = tail / (d + 1)
        count += factor
        count %= MOD
        x -= factor * d
    if n > 0:
        count += 1

    return count


def main():
    s = solution(17)
