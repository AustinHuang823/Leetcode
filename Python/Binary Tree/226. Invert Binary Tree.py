import DS
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invT(root):
            if not root: return
            root.left, root.right = root.right, root.left
            invT(root.right)
            invT(root.left)
        invT(root)
        return root




if __name__ == '__main__':
    root = DS.arr2TreeNode([4,2,7,1,3,6,9])
    sol = Solution()
    print(sol.invertTree(root))