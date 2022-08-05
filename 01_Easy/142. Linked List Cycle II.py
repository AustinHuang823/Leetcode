from DS import ListNode
import DS
from typing import Optional

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        From the two pointer solution of Linked List Cycle
        The solution is from https://leetcode.com/problems/linked-list-cycle-ii/discuss/44793/O(n)-solution-by-using-two-pointers-without-change-anything
        If found a meeting point, one pointer start from the start, the other pointer starts from the meeting point
        the next time them meet, it is the head of the cycle
        """
        node_map = set()
        while head:
            print(head.val)             
            if head in node_map: 
                return head
            else:
                node_map.add(head)
                head = head.next
        
        return 


if __name__ == '__main__':
    arr = [3,2,0,-4]
    head = DS.arr2LinkedNode(arr)
    start = head.next
    i = head
    while i.next:
        i = i.next
    i.next = start
    sol = Solution()
    ans = sol.detectCycle(head)
    print(ans.val)