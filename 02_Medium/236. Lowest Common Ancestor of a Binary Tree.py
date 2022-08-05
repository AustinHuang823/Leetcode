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
        return self.dfs(root, p, q)
            
    def dfs(self, root, p, q):
        if root == None: return None #quick test for root = [None] case
        if p.val == root.val or q.val == root.val : return root #once we find p or q, return it
        
        r, l = self.dfs(root.right, p, q), self.dfs(root.left, p, q) #establishing finding path
        if l and r: return root #if both l and r are not None, we return root here because the root is common anscestor in this case
        return l or r #else case we return l or r if one of them isn't None
        
            
            
if __name__ == '__main__':
    root = DS.arr2TreeNode([3,5,1,6,2,0,8,None,None,7,4])
    p = DS.arr2TreeNode([4])
    q = DS.arr2TreeNode([8])
    sol = Solution()
    ans = sol.lowestCommonAncestor(root, p , q)
    print(ans.val)