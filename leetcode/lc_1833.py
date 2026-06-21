from collections import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        """
            costs of length n where costs[i] is the price of the ith ice cream bar in coins

            he has c coins and wants to buy as many ice cream bars as possible

        """

        amount = 0
        costs.sort()
        for i in range(len(costs)):
            if costs[i] <= coins:
                amount += 1
                coins -= costs[i]
            else:
                return amount
        return amount
