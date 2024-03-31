# Definition for a binary tree node.
from typing import Optional
import DS as DS

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        self.hi = float("-inf")

        def dfs(root, num):
            if not root: return
            if not root.left and not root.right:
                self.hi = max(self.hi, num)
            
            dfs(root.left, num+1)
            dfs(root.right, num+1)

        dfs(root,1)

        return self.hi

if __name__ == '__main__':
    root = DS.arr2TreeNode([3,9,20,None,None,15,7])
    sol = Solution()
    print(sol.maxDepth(root))