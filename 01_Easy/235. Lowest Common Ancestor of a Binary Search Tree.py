# Definition for a binary tree node.
import DS
from DS import TreeNode
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if root.val > p and root.val > q:#p.val q.val in leetcode
                root = root.left
            elif root.val < p and root.val < q:
                root = root.right
            else:
                return root
            
            
if __name__ == '__main__':
    root = DS.arr2TreeNode([6,2,8,0,4,7,9,None,None,3,5])
    p = 2
    q = 8
    sol = Solution()
    ans = sol.lowestCommonAncestor(root, p , q)
    print(ans.val)