from typing import Optional
import collections
import DS
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return

        this, next = collections.deque([root]), collections.deque([])
        prev = None
        while this:
            cur = this.popleft()
            if prev:
                prev.next = cur
            if cur.left:
                next.append(cur.left)
            if cur.right:
                next.append(cur.right)
            if not this:
                this, next, prev = next, collections.deque([]), None
            else:
                prev = cur
        return root

if __name__ == "__main__":
    root = DS.arr2TreeNode([1,2,3,4,5,6,7])
    sol = Solution()
    print(sol.connect(root))