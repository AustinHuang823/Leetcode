from DS import TreeNode
import DS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.recursive_dfs(root, float('-inf'), float('inf'))
    
    def recursive_dfs(self, root, min, max):
        if not root:
            return True
        if not min < root.val < max:
            return False
        
        return self.recursive_dfs(root.left, min, root.val) and self.recursive_dfs(root.right, root.val, max)



class Solution2:
    def isValidBST(self, root: TreeNode) -> bool:
        def recurse(root, low, high):
            if not root:
                return True
            if not low < root.val < high:
                return False
            return recurse(root.left,low, root.val) and recurse(root.right,root.val,high)
        return recurse(root,low=float('-inf'),high=float('inf'))
    
if __name__ == '__main__':    
    root = DS.arr2TreeNode([2,1,3])
    sol = Solution()
    sol2 = Solution2()
    print(sol.isValidBST(root),sol2.isValidBST(root))
    
    