# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
import DS
from DS import ListNode

#https://leetcode.com/problems/reverse-linked-list-ii/discuss/30709/Talk-is-cheap-show-me-the-code-(and-DRAWING)

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right: return head
        p = dummy = ListNode(None)
        dummy.next = head
        for i in range(left-1): p = p.next
        tail = p.next

        for i in range(right - left):
            tmp = p.next                  # a)
            p.next = tail.next            # b)
            tail.next = tail.next.next    # c)
            p.next.next = tmp             # d)
        return dummy.next
        
if __name__ == '__main__':
    head = DS.arr2LinkedNode([1,2,3,4,5])
    left = 2
    right = 4
    sol = Solution()
    ans = sol.reverseBetween(head, left, right)
    DS.print_ListNode(ans)