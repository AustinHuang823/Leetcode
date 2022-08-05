import DS
from typing import Optional
from DS import TreeNode
from typing import List 
import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
class Solution_DFS:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans = []
        this_level = [root]
        if root:
            while this_level:
                this_level_val = []
                next_level = []   
                for node in this_level:
                    this_level_val.append(node.val)
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
                ans.append(this_level_val)
                this_level = next_level

        return ans
    
class Solution_BFS:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []
        q = collections.deque()
        q.append(root)
        
        while q:
            level = []
            qLen = len(q)
            
            for i in range(qLen):
                node = q.popleft()
                
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                
            if level:
                res.append(level)
                
        return res


if __name__ == '__main__':
    root = DS.arr2TreeNode([3,9,20,None,None,15,7])
    sol = Solution_DFS()
    ans = sol.levelOrder(root)
    print(ans)