from DS import ListNode
import DS
from typing import Optional
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow




if __name__ == '__main__':
    head = DS.arr2LinkedNode([1,2,3,4])
    sol = Solution()
    ans = sol.middleNode(head)
    DS.print_ListNode(ans)