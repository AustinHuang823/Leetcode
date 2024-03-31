# Definition for a binary tree node.
from importlib.resources import path
from typing import Optional, List
import DS as DS
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(root, currPath):
            if not root: return
            currPath.append(root.val)
            if not root.right and not root.left:
                if sum(currPath) == targetSum:
                    res.append(currPath.copy())
            dfs(root.left, currPath)
            dfs(root.right, currPath)
            currPath.pop()
        
        dfs(root, [])
        return res
                
        
if __name__ == '__main__':
    root = DS.arr2TreeNode([5,4,8,11,None,13,4,7,2,None,None,5,1])
    targetSum = 22
    sol = Solution()
    print(sol.pathSum(root,targetSum))