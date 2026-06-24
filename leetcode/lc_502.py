from collections import deque
import heapq
from typing import List

class Solution:
    def findMaximizedCapital_1(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        """
        Suppose leetcode will start its IPO soon
        in order to sell a good price of its share to VC
        leetcode would like to work on some projects to increase capital before the IPO
        since it has limited resources, it can only finish
        at most k distinct projects before the IPO
        help leetcode design the best way to maximize its total capital after finishing at most k distinct projects

        you are given n projects where the ith project has a pure profit of profits[i] and a minimum capital of capital[i] is needed to start it

        initially we have w capitial when you finish a project you gain its profit and profit will be added to your total capitial

        pick at most k distinct porjects to maximize your final capital and return the final capital


        Example 1:
        w = 0
        k = 2
        [1,2,3]
        [0,1,1]

        output: 4


        maximise profit

        heap

        desc, asc
        (profit,cost)

        queue


        w = 99

        k = 2

        [0,100]
        [1,100]

        """

        max_heap = list((-a,b) for a,b in zip(profits,capital))

        heapq.heapify(max_heap)
        # k * log(N) * q
        while k > 0:
            q = deque([])
            # remove the projects that are too expensive
            while max_heap and max_heap[0][1] > w:
                q.appendleft(heapq.heappop(max_heap))
            # we could not start any project
            # print(f"queue {q} and max_heap {max_heap} and curr_cap {w}")
            if not max_heap:
                return w
            prof, cost = heapq.heappop(max_heap)
            prof = -prof
            k -= 1
            w += prof
            for _ in range(len(q)):
                heapq.heappush(max_heap, q.popleft())
        return w


    def findMaximizedCapital_2(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        """
            Intuition behind the neetcode optimal solution

            - My first approach tried to maximise IPO by first filtering the heap
            and adding all the projects we could not afford at that time to a queue or q

            - Then checking if the max_heap was empty that can happen if we cannot afford anything and we drained the entire max_heap, but if we could afford something then the best profit at that time will be at the top of the heap so we add it to our capital

            - now that capital increased maybe we could starrt the ones we could not do before so i go through the queue and add them back to the heap which is the issue

            so my time complexity was k * log(N) * q * log(n)
            which can simplify to k * log(N) * q which is not really good can we do better ???


            Yes we can

            - The neetcode optimal solution is built on the opposite of what i did
            so instead of adding everything and then filtering stuff we could not get at that point in time we simplify the logic

            - How ??

            - Well we only deal with the ones we can buy at first how ?? we use a min heap with (cost,prof) and we add all the optionswe can buy first

            - and then add the max to our profit then continue the loop

            the optimization is that we do not need to do the last  * q step of adding the projects we filtered at the beginning back into the queue and we maintain 2 heaps instead one is the ones we can afford which is a min_heap and and then the max_heap gives us the best choice of the ones we can afford so we can maximise for the next step

            I will call this 2 heap techique eventual discovery approach

            so this works by unlocking levels we can start with then
            picking the best boss on each level to maximise our chances for the boss on the next level
        """
        # Put the ones we can afford in a min_heap
        min_heap = [(c,p) for c,p in zip(capital,profits)]
        # The ones we can afford but we pick the max of that each time
        max_heap = []
        heapq.heapify(min_heap)

        while k > 0:

            # We are checking for bosses in the current level we can currenltly reach eventually we might be able to access even more levels or floors
            while min_heap and min_heap[0][0] <= w:
                c,p = heapq.heappop(min_heap)
                heapq.heappush(max_heap,-1 * p)

            # if we have checked all the levels from smallest to biggest and we could not unlock any level then there is no floor we can unlock break early
            if not max_heap:
                break

            # We maximise our profit with the items we can unlock on this level by using that max_heap
            prof = -1 * heapq.heappop(max_heap)
            w += prof
            k -= 1
        return w
