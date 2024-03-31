from typing import Optional
from typing import List
import DS as DS
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        this_level = 0
        res = []
        
        #function
        def buildlist(root, this_level, res):
            if root:
                if this_level >= len(res):
                    res.append([])
                res[this_level].append(root.val)
                
                if root.left: buildlist(root.left, this_level + 1, res)
                if root.right: buildlist(root.right, this_level + 1, res)
            
        buildlist(root, 0 , res)
        
        for i in range(len(res)):
            if i % 2 == 1:
                res[i] = list(reversed(res[i]))
        
        return res
        
        #res = [[3], [9, 20], [15,7]]
        
        #function to reverse res[1],res[3].....etc.

        
if __name__ == '__main__':
    root = DS.arr2TreeNode([3,9,20,None,None,15,7])
    sol = Solution()
    print(sol.zigzagLevelOrder(root))