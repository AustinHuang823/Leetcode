# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        head = dummy
        while list1 or list2:
            if not list1:
                dummy.next = list2
                break
            elif not list2:
                dummy.next = list1
                break
            elif list1.val >= list2.val:
                dummy.next = list2
                list2 = list2.next
            else:
                dummy.next = list1
                list1 = list1.next
            dummy = dummy.next
        
        return head.next

if __name__ == "__main__":
    list1 = [1,2,4]
    list2 = [1,3,4]
    sol = Solution()
    print(sol.mergeTwoLists(list1, list2))