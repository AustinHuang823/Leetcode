# Definition for a binary tree node.
from typing import Optional, List
import DS as DS
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            temp = root
            root = TreeNode(val)
            root.left = temp
            return root
        
        origin = root
        h = 1
        def dfs(root,h):
            h += 1
            if h == depth:
                self.buildtree(root, val)
            
            if root.left: dfs(root.left, h)
            if root.right: dfs(root.right, h)
        
        dfs(root, h)
        
        return origin
        
    def buildtree(self, root, val):
        if root.right:
            tempR = root.right
            root.right = TreeNode(val)
            root.right.right = tempR
        else: 
            root.right = TreeNode(val)
            
        if root.left:
            tempL = root.left
            root.left = TreeNode(val)
            root.left.left = tempL
        else: 
            root.left = TreeNode(val)
        
        
if __name__ == '__main__':
    sol = Solution()
    root = DS.arr2TreeNode([4,2,6,3,1,5])
    val = 1
    depth = 2
    print(sol.addOneRow(root,val,depth))