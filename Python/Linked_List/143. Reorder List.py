import DS
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # dummy = ListNode(0)
        #find middle
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse
        prev, curr = None, slow.next
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        slow.next = None

        #merge
        head1, head2 = head, prev
        while head2:
            curnext = head1.next
            head1.next = head2
            head1 = head2
            head2 = curnext

class SolutionTLE:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def findlast(root):
            prev = ListNode(0)
            prev.next = root
            while root:
                prev, root = prev.next, root.next
            return prev
        
        dummy = ListNode(0)
        dummy.next = head
        while head:
            if not head.next or not head.next.next: break
            cur_next = head.next
            head.next = findlast(head)
            head.next.next = cur_next
            head = head.next.next
        
        return dummy.next

if __name__ == '__main__':
    head = DS.arr2LinkedNode([1,2,3,4,5])
    sol = SolutionTLE()
    print(DS.print_ListNode(sol.reorderList(head)))