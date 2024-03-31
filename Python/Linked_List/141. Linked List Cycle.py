# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from itertools import count
from typing import Optional
import DS as DS

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        #memo
        visited = []
        
        #while
        while head:
            if head.next in visited:
                return True
            visited.append(head)
            head = head.next
        
        return False

        
if __name__ == '__main__':
    head = DS.arr2LinkedNode([3,2,0,-4] )
    pos = 1
    sol = Solution()
    print(sol.hasCycle(head, pos))