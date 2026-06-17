class Solution:
    def minSwaps(self, s: str) -> int:
        """
            Given a binary string s

            return the min number of character swaps to make it alternating
            or -1 if it is impossible

            The string is called alternating
            if no two adjacent characters are equal
            for example 010 or 1010 are alternating
            while the string 0100 is not


            111000 -> 10

            011

            1111 000


        """

        zeros = s.count("0")
        ones = s.count("1")
        N = zeros + ones
        if abs(ones - zeros) > 1:
            return -1

        c1,c2 = "0", "1"
        r1 = r2 = 0
        for i in range(N):
            r1 += 1 if s[i] != c1 else 0
            r2 += 1 if s[i] != c2 else 0
            c1 = "0" if c1 != "0" else "1"
            c2 = "0" if c2 != "0" else "1"

        if r1 == 0 or r2 == 0:
            return 0

        r1 = r1 // 2
        r2 = r2 // 2

        # r1 = mismatches for "010101..." pattern (starts with 0)
        # r2 = mismatches for "101010..." pattern (starts with 1)
        #
        # When zeros == ones (even length), both patterns are valid, pick min
        # When ones > zeros  (odd length), only "1010...1" works -> r2
        # When zeros > ones  (odd length), only "0101...0" works -> r1
        # The other pattern would need more 0s or 1s than we have
        return min(r1,r2) if zeros == ones else r2 if ones > zeros else r1

