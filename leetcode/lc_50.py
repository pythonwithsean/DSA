class Solution:
    def myPow(self, x: float, n: int) -> float:


        """
            pow(x,n)

            x^n

            2 * 2 * 2 * 2 * 2 * 2 ... n


            5^10

            5 * 5 * 5 * 5 * 5

            5^5 = y * y


            5^6

            5^7

            5^1 1
            5^2 1
            5^4 1

            1
            5^100
           0 1 2 3 4 5 6

           1 2 4 8 16 32 64

           0 0  1 0 0 1 1


           32 = 16 * 2

            5^4 * 5^32 * 5^64

            (5^4)^2
            5^4*2
            5^8

            p = 5^32
            p = p * p


            b^x = y
            b^x+1 = y * b



            2^10 = 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2
            2^10 = 2^2 * 2^2 * 2^2 * 2^2 * 2^2
            2^10 = 2^4 * 2^4 * 2^2
            2^10 = 2^8 * 2^2

            8421
            1010


                      8421
            bin(10) = 1010

            How do we get:
            2^10 = 2^2 * 2^8
            Notice the bits in bin(10) are on for 2 and 8
            Can we just build from bottom-up, and using only the powers that are a '1'

            2^10      8421
            bin(10) = 1010

            1010

            result = 4       repesents: (2^2)

            prod = 4


            2^1 = 0
            2^2 = 1
            2^4 = 0 <
            2^8 = 1




        """
        # handle negative
        res = 1
        prod  = x
        b = bin(n)[2:]
        for i in range(len(b)-1,-1,-1):
            if b[i] == "1":
                print(prod)
                res *= prod
            prod *= prod
        if n < 0:
            return 1 / res
        return res
