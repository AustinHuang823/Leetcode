import DS
import collections
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        this_lvl = collections.deque([root])
        next_lvl = collections.deque()
        while this_lvl:
            cur = this_lvl.popleft()
            if not cur:
                break
            if this_lvl:
                cur.next = this_lvl[0]
            else:
                cur.next = None

            if cur.left:
                next_lvl.append(cur.left)
            if cur.right:
                next_lvl.append(cur.right)
            
            if not this_lvl:
                this_lvl, next_lvl = next_lvl, collections.deque()
        
        return root



if __name__ == '__main__':
    root = DS.arr2TreeNode([1,2,3,4,5,None,7])
    sol = Solution()
    print(sol.connect(root))