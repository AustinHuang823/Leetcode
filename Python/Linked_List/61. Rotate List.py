from typing import Optional
import DS
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        dummy = ListNode(None)
        dummy.next = head
        start = head

        linklen = 0
        while head:
            end = head
            head = head.next
            linklen += 1
        

        pivot = k % linklen
        if pivot:
            head = dummy.next
            for _ in range(linklen-pivot):
                prev = head
                head = head.next
            dummy.next = head
            end.next = start
            prev.next = None
            
        
        return dummy.next
        



if __name__ == '__main__':
    head = DS.arr2LinkedNode([1,2,3,4,5])
    k = 6
    sol = Solution()
    DS.print_ListNode(sol.rotateRight(head,k))