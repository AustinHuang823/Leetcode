from typing import Optional
import DS
from DS import ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        
        elif not list2:
            return list1
        elif not list1:
            return list2
        
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2




        
class Solution2:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            # both list1 and list2 are empty list
            return None
        
        elif not list1:
            # list1 is empty, return list2
            return list2
        
        elif not list2:
            # list2 is empty, return list1
            return list1
        
        
        # General cases, compare node value and merge
        
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


if __name__ == '__main__':
    list1 = DS.arr2LinkedNode([1,1,2,3,3])
    list2 = DS.arr2LinkedNode([1,3,4])
    sol = Solution()
    ans = sol.mergeTwoLists(list1, list2)
    DS.print_ListNode(ans)