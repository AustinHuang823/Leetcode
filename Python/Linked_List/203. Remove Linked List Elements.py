# Definition for singly-linked list.
from typing import Optional
import DS as DS
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head: return None
        dummy = cur = ListNode(0)
        dummy.next = head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
                
        return dummy.next
                
                
        
        
if __name__ == '__main__':
    head = DS.arr2LinkedNode([1,2,6,3,4,5,6])
    val = 6
    sol = Solution()
    print(sol.removeElements(head, val))