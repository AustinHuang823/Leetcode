# Definition for singly-linked list.
from typing import Optional
import DS as DS
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev
        
        
if __name__ == '__main__':
    head = DS.arr2LinkedNode([1,2,3,4,5])
    pos = 1
    sol = Solution()
    print(sol.hasCycle(head, pos))