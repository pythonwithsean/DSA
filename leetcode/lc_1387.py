class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        """
            The power of an integer x is defined as the number
            of steps needed to transform from x into 1
            using the followig steps

            if x is even then x = x / 2
            if x is odd then x = 3 * x + 1

            For example the power of x = 3 is 7


            given lo, high and k the task is to sort all integers in the interval [lo,hi] by the power value in ascending order if two or more integers have the same power value sort them in asc order

            return the kth integer in the range lo,hi sorted by the power value

            x ->
        """
        arr = [0] * (hi - lo + 1)
        memo = {}
        def fn(x):
            if x ==1:
                return 0
            if x in memo :
                return memo[x]
            if x % 2 == 0:
                memo[x] = 1 + fn(x // 2)
                return memo[x]
            else:
                memo[x] = 1 + fn(3 * x + 1)
                return memo[x]

        curr = 0
        for i in range(lo,hi+1):
            arr[curr] = (i,fn(i))
            curr += 1
        arr.sort(key=lambda x: (x[1],x[0]))
        return arr[k-1][0]


       