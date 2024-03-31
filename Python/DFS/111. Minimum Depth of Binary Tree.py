# Definition for a binary tree node.
from typing import Optional
import DS

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:


        self.min_lvl = float('inf')

        def dfs(root, cur_lvl):
            if not root:
                return

            if not root.right and not root.left:
                self.min_lvl = min(cur_lvl, self.min_lvl)
                return
            
            if root.right:
                dfs(root.right, cur_lvl+1)
            if root.left:
                dfs(root.left, cur_lvl+1)

        
        dfs(root, 1)

        return self.min_lvl if root else None


if __name__ == '__main__':
    root = DS.arr2TreeNode([3,9,20,None, None,15,7])
    sol = Solution()
    print(sol.minDepth(root))