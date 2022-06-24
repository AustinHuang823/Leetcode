from typing import List

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def minCameraCover(self, root: TreeNode) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, par = None):
            
            if node:
                dfs(node.left, node)
                dfs(node.right, node)

                if (par is None and node not in covered or
                        node.left not in covered or node.right not in covered):
                    self.res += 1
                    covered.update({node, par, node.left, node.right})

        self.res = 0
        covered = {None}
        dfs(root)
        return self.res
        
class Solution2:
    def minCameraCover(self, root):
        self.res = 0
        def dfs(root):
            if not root: return 2
            l, r = dfs(root.left), dfs(root.right)
            if l == 0 or r == 0:
                self.res += 1
                return 1
            return 2 if l == 1 or r == 1 else 0
        return (dfs(root) == 0) + self.res

if __name__ == '__main__':
    sol = Solution2()
    root = [0,0,None,0,None,0,None,None,0]
    print(sol.minCameraCover(root))