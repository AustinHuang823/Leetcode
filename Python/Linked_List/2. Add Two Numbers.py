from typing import Optional
import DS as DS

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode(0)
        #divide two situation
        add = 0
        while l1 or l2 or add:
            cur_val = 0
            if l1:
                cur_val += l1.val
                l1 = l1.next
            if l2:
                cur_val += l2.val
                l2 = l2.next
            cur_val += add
            if cur_val >= 10:
                cur.next = ListNode(cur_val - 10)
                add = 1
            else:
                cur.next = ListNode(cur_val)
                add = 0
            cur = cur.next
        
        return dummy.next
            

if __name__ == '__main__':
    l1 = DS.arr2LinkedNode([2,4,3])
    l2 = DS.arr2LinkedNode([5,6,4])
    sol = Solution()
    print(sol.addTwoNumbers(l1, l2))