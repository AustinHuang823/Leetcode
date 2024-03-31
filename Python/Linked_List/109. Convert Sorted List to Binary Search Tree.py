from typing import Optional
import DS

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        
        prev = mid = fast = head
        while fast and fast.next:
            prev = mid
            mid = mid.next
            fast = fast.next.next
        
        if head == mid:
            return TreeNode(mid.val)
        prev.next = None
        return TreeNode(mid.val, self.sortedListToBST(head), self.sortedListToBST(mid.next))



if __name__ == "__main__":
    head = DS.arr2LinkedNode([-10,-3,0,5,9])
    sol = Solution()
    print(sol.sortedListToBST(head))