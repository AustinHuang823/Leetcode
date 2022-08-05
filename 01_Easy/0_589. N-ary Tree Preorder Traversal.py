import DS
from typing import List
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
       if not root:
           return None
       
       ans = []
       ans.append(root.val)
       for n in root.children:
           ans += self.preorder(n)
       
       return ans
        
        
if __name__ == '__main__':
    root = DS.arr2LinkedNode([1,None,3,2,4,None,5,6])
    sol = Solution()
    ans = sol.preorder(root)
    DS.print_ListNode(ans)