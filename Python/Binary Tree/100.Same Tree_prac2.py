from typing import Optional
from typing import List
import DS
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)



if __name__ == '__main__':
    p = DS.arr2TreeNode([1,None,2,3,4])
    q = DS.arr2TreeNode([1,None,2,3])
    sol = Solution()
    print(sol.isSameTree(p, q))