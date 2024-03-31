from typing import Optional
import DS

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(None)
        dummy.next = head
        prev, cur = dummy, dummy.next
        duplicate = False
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
                duplicate = True
            elif duplicate:
                prev.next = cur.next
                cur = cur.next
                duplicate = False
            else:
                prev, cur = prev.next, cur.next
                duplicate = False
        
        if duplicate:
            prev.next = None
        
        return dummy.next




if __name__ == '__main__':
    head = [1,1]