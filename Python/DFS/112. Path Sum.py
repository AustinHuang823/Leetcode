from typing import Optional
import DS as DS
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        def dfs(root, sum):
            if not root:
                return 
            sum += root.val
            if not root.right and not root.left:
                if sum == targetSum:
                    return True
            
            return dfs(root.left, sum) or dfs(root.right, sum)
        
        return dfs(root, 0)
            
            
        
if __name__ == '__main__':
    root = DS.arr2TreeNode([5,4,8,11,None,13,4,7,2,None,None,None,1])
    targetSum = 22
    sol = Solution()
    print(sol.hasPathSum(root, targetSum))