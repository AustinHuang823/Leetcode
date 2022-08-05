# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from platform import node
from typing import Optional
import DS
from DS import TreeNode

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        parent = root
        stack = [root.right, root.left]
        
        while stack:
            node = stack.pop()
            if not node:
                continue
            parent.left = None
            parent.right = node
            parent = node
            stack.append(node.right)
            stack.append(node.left)
            print(stack)
        return root

if __name__ == '__main__':
    root = DS.arr2TreeNode([1,2,5,3,4,None,6])
    sol = Solution()
    ans = sol.flatten(root)
    print(ans.val)