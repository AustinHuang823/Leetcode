# Definition for singly-linked list.
from typing import Optional
import DS as DS

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #while loop
        head = cur = ListNode(0)
        while list1 and list2:
            #compare the value of heads of list1 and list2
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            
            cur = cur.next
                    
        cur.next = list1 or list2
                

        return head.next
            
        
        
if __name__ == '__main__':
    list1 = DS.arr2LinkedNode([1,2,4])
    list2 = DS.arr2LinkedNode([1,3,4])
    sol = Solution()
    print(sol.mergeTwoLists(list1, list2))