from typing import Optional
from typing import List
import DS
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        res = []

        def helper(root, is_root):
            if not root:
                return None
            this_root_delete = root.val in to_delete_set
            if is_root and not this_root_delete:
                res.append(root)
            root.left = helper(root.left, this_root_delete)
            root.right = helper(root.right, this_root_delete)
            return None if this_root_delete else root
        
        helper(root, True)
        return res
            




if __name__ == '__main__':
    root = DS.arr2TreeNode([1,2,3,4,5,6,7]) 
    to_delete = [3,5]
    sol = Solution()
    print(sol.delNodes(root,to_delete))
