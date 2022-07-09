from typing import List
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            # both l1 and l2 are empty list
            return None
        
        elif not list1:
            # l1 is empty, directly return l2
            return list2
        
        elif not list2:
            # l2 is empty, directly return l1
            return list1
        
        
        ## General cases
        # Compare node value and merge
        
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2




if __name__ == '__main__':
    list1 = [1,2,4]
    list2 = [1,3,4]
    sol = Solution()
    print(sol.mergeTwoLists(list1, list2))