class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        """
            You are given 3 ints l,r and k

            An integer y is said to be perfect kth power if there ecists an integer x
            such taht y = x^k

            return the number of integerds y in rangen of l to r

            l -> r+1 are ranges

            What does perfecting the kth power mean -> if there exists an integer x such that y = x^k



            1,2,3,4,5,6,7,8,9

            1^3 -> 1
            2^3 -> 8
            3^3 -> 27


            k = 1

            1 4 9, 16, 25



            8 // 3 = 3 // 1 =


            2 * 2 * 2 = 8

            x^3 = 8
            x = k/8

            2 * 2 * 2 * 2
            k = 4

            32 // 4 = 8 / 4 = 2 / 4 = 1
            33 / 4 = 8

            Geometric sequence

            1 4 9 16 25


        """

        if k == 1:
            return (r - l + 1)

        curr = 0
        res = 0
        while True:
            if curr**k > r:
                break
            if l <= curr ** k <= r:
                res += 1
            curr += 1
        return res


        