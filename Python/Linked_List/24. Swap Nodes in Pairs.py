from typing import Optional
import DS

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return
        dummy = ListNode(None)
        dummy.next = head
        prev, cur = dummy, head
        while cur and cur.next:
            prev.next = cur.next
            cur.next = cur.next.next
            prev.next.next = cur
            prev, cur = cur, cur.next
        
        return dummy.next





if __name__ == '__main__':
    head = DS.arr2LinkedNode([1,2,3,4])
    print(Solution().swapPairs(head))