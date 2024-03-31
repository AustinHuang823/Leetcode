from typing import Optional
import DS as DS
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, depth):
            if not root:
                return depth
            return max(dfs(root.right, depth + 1), dfs(root.left, depth + 1))
                    
        return dfs(root, 0)
        
if __name__ == '__main__':
    root = DS.arr2TreeNode([3,9,20,None,None,15,7])
    sol = Solution()
    print(sol.maxDepth(root))