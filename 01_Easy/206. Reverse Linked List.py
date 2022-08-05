from typing import Optional
import DS
from DS import ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head, prev=None):
        if not head:
          return prev
  
        curr, head.next = head.next, prev
        if curr:
            print(curr.val)
        if head:
            print(head.val)
        if prev:
            print(prev.val)
        return self.reverseList(curr, head)

class Solution3:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            curr = head
            # print('curr:', curr.val)
            
            head = head.next
            # if head: print('head:', head.val)
            # else: print(None)
            
            curr.next = prev
            # if curr.next: print('curr.next:', curr.next.val)
            # else: print(None)
            
            prev = curr
            # print('prev:', prev.val)
            # print('loop end')
        return prev
    
class Solution2:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        return self._reverse(head)

    def _reverse(self, node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self._reverse(n, node)
        

if __name__ == '__main__':
    head = DS.arr2LinkedNode([1,2,4])
    sol = Solution3()
    ans = sol.reverseList(head)
    DS.print_ListNode(ans)