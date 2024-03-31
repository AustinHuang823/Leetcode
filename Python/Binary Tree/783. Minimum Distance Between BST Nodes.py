import collections
from typing import Optional
import DS
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution1:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        q = collections.deque([root])
        num_list = []
        while q:
            node = q.popleft()
            num_list.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        num_list = sorted(num_list)

        min_res = float('inf')
        for i in range(len(num_list)-1):
            min_res = min(num_list[i+1]-num_list[i], min_res)
        
        return min_res

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        nums = []

        def dfs(root):
            if not root: return

            dfs(root.left)
            nums.append(root.val)
            dfs(root.right)
        
        dfs(root)
        min_diff = float('inf')
        for i in range(len(nums)-1):
            min_diff = min(nums[i+1]-nums[i],min_diff)
        return min_diff
            

if __name__ == '__main__':
    root = DS.arr2TreeNode([4,2,6,1,3])
    sol = Solution()
    print(sol.minDiffInBST(root))
