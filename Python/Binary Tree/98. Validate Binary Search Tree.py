# Definition for a binary tree node.
import DS as DS
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.recurse(root, float("-inf"), float("inf"))
    def recurse(self, root, low, high):
        if not root: return True
        if root.val <= low or root.val >= high:
            return False
        return self.recurse(root.left, low, root.val) and self.recurse(root.right, root.val, high)

if __name__ == '__main__':
    sol = Solution()
    root = DS.arr2TreeNode([2,1,3])
    val = 1
    depth = 2
    print(sol.isValidBST(root))