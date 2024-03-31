# Definition for a binary tree node.
import DS as DS
from typing import Optional, List
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack, level_stk = collections.deque(), collections.deque()
        res, this_level, level = [], [], 0
        if root: 
            stack.append(root)
            level_stk.append(level)
        while stack:
            node, lvl = stack.popleft(), level_stk.popleft()
            if node.left:
                stack.append(node.left)
                level_stk.append(lvl+1)
            if node.right:
                stack.append(node.right)
                level_stk.append(lvl+1)
            
            this_level.append(node.val)
            if level_stk:
                if level_stk[0] != lvl:
                    res.append(this_level)
                    this_level = []
            else:
                res.append(this_level)


        return res

if __name__ == '__main__':
    root = DS.arr2TreeNode([3,9,20,None,None,15,7])
    sol = Solution()
    print(sol.levelOrder(root))