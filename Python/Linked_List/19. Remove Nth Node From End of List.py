# Definition for singly-linked list.
from itertools import count
from typing import Optional
import DS as DS
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        slow = head
        # advance fast to nth position
        for i in range(n):
            fast = fast.next
            
        if not fast:
            return head.next
        # then advance both fast and slow now they are nth postions apart
        # when fast gets to None, slow will be just before the item to be deleted
        while fast.next:
            slow = slow.next
            fast = fast.next
        # delete the node
        slow.next = slow.next.next
        return head

class Solution1:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        # establish a new listnode
        dummy = cur = ListNode(0)
        
        # go through head and count length
        while head:
            count += 1
            cur.next = head
            head, cur = head.next, cur.next
        
        # get count - n and go through the established list 
        target = count - n #3
        pos = 0
        cur = dummy.next        
        if target == 0:
            return cur.next
                
        while pos < target - 1:
            pos += 1
            cur = cur.next

        
        if cur.next and cur.next.next:
            cur.next = cur.next.next
        elif cur.next and not cur.next.next:
            cur.next = None
        else:
            return
        
        return dummy.next
        
class Solution2:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow, fast = head, head
        dummy = ListNode(0)
        dummy.next = slow
        
        for i in range(n):
            fast = fast.next
        
        if not fast:
            return head.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        
        return dummy.next
        
if __name__ == '__main__':
    head = DS.arr2LinkedNode([1,2,3,4,5])
    n = 2
    sol = Solution2()
    print(sol.removeNthFromEnd(head, n))