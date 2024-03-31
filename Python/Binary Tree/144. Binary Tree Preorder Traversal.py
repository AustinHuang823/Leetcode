# Definition for a binary tree node.
from typing import Optional, List
import DS as DS
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution1:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
    
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, res = [root], []
        #while add root into stack
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res
            
        
if __name__ == '__main__':
    sol = Solution()
    root = DS.arr2TreeNode([1,2,3,4,5])
    print(sol.preorderTraversal(root))