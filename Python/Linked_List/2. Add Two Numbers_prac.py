from typing import Optional
import DS
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        head = ListNode(0)
        dummy.next = head

        add1 = False
        while l1 or l2 or add1:
            if l1:
                head.val += l1.val
            if l2:
                head.val += l2.val
            if add1:
                head.val += 1

            if head.val // 10:
                add1 = True
            else:
                add1 = False
            
            head.val %= 10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            if l1 or l2 or add1:
                head.next = ListNode(0)
                head = head.next

        
        return dummy.next



if __name__ == '__main__':
    l1 = DS.arr2LinkedNode([9,9] )
    l2 = DS.arr2LinkedNode([9])
    sol = Solution()
    print(DS.print_ListNode(sol.addTwoNumbers(l1, l2)))
