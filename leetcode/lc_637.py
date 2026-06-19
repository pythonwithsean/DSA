from collections import deque, defaultdict
from typing import Optional, TreeNode,List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        levels = defaultdict(tuple)
        level = 0
        q = deque([(root,level)])
        res = []
        while q:
            curr,lvl = q.popleft()
            if lvl not in levels:
                levels[lvl] = (0,0)
            curr_val,size = levels[lvl]
            levels[lvl] = (curr_val + curr.val, size + 1)
            if curr.left:
                q.append((curr.left,lvl + 1))
            if curr.right:
                q.append((curr.right,lvl + 1))
        for l in levels.values():
            s, size = l
            res.append(s / size)
        return res
