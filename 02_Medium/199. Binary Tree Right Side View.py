import DS
from typing import Optional
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        
        res, nxtL= [], [root] #if root else []
        while nxtL:
            res.append(nxtL[-1].val) # right most val as to output
            # print(res)
            curL, nxtL = nxtL, []
            for i in curL: # build next level
                if i.left: nxtL.append(i.left)
                if i.right: nxtL.append(i.right)
        return res
        
if __name__ == '__main__':
    root = DS.arr2TreeNode([1,2,3,None,5,None,4])
    sol = Solution()
    print(sol.rightSideView(root))