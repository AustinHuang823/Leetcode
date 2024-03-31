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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack_p, stack_q = collections.deque(), collections.deque()
        if p and q:
            stack_p.append(p)
            stack_q.append(q)
        elif p or q:
            return False

        while stack_p and stack_q:
            node_p, node_q = stack_p.popleft(), stack_q.popleft()
            if node_p.val != node_q.val:
                return False
            if node_p.left and node_q.left:
                stack_p.append(node_p.left)
                stack_q.append(node_q.left)
            elif node_p.left or node_q.left:
                return False
            if node_p.right and node_q.right:
                stack_p.append(node_p.right)
                stack_q.append(node_q.right)
            elif node_p.right or node_q.right:
                return False
        return True
            
if __name__ == '__main__':
    p = DS.arr2TreeNode([1,None,2,3])
    q = DS.arr2TreeNode([1,None,2,3])
    sol = Solution()
    print(sol.isSameTree(p, q))


