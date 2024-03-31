# Definition for a binary tree node.
from typing import Optional
import DS as DS
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root.right, root.left)
        # return root.left root right
        
    def isMirror(self, right, left):
        if right == None and left == None:
            return True
        
        if right and left:
            if right.val != left.val:
                return False
        elif right == None or left == None:
            return False
            
        
        #iter function
        return self.isMirror(right.right, left.left) and self.isMirror(right.left, left.right)
    
        
        
if __name__ == '__main__':
    root = DS.arr2TreeNode([1,2,2,3,4,4,3])
    pos = 1
    sol = Solution()
    print(sol.isSymmetric(root))