# Definition for a binary tree node.
from typing import Optional, List
import DS as DS
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        deque = collections.deque()
        res = []
        if root: deque.append(root)
        while deque:
            level, size = [], len(deque)
            for i in range(size):
                node = deque.popleft()
                level.append(node.val)
                if node.left: deque.append(node.left)
                if node.right: deque.append(node.right)
                
            res.append(level)
            
        
        return res[::-1]
            
            
if __name__ == '__main__':
    root = DS.arr2TreeNode([1,2,3,4,None,None,5])
    sol = Solution()
    print(sol.levelOrderBottom(root))