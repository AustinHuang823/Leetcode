from typing import Optional
import DS
from DS import ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur=head
        while cur:
            while cur.next and cur.next.val==cur.val:
                cur.next=cur.next.next
            cur=cur.next
        return head


class Solution2: 
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        setlist_head = ListNode(None)
        setlist = setlist_head
        while head:
            if head.val != setlist.val:
                setlist.next = head
                setlist = setlist.next
            head = head.next
        setlist.next = None
        return setlist_head.next
        

if __name__ == '__main__':
    head = DS.arr2LinkedNode([1,1,2,3,3])
    sol = Solution2()
    ans = sol.deleteDuplicates(head)
    DS.print_ListNode(ans)