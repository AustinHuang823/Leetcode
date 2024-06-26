# Definition for singly-linked list.
from typing import Optional
import DS as DS
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
            
        return True
        
        
if __name__ == '__main__':
    head = DS.arr2LinkedNode([1,2,2,1])
    sol = Solution()
    print(sol.isPalindrome(head))