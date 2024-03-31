"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from typing import Optional
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        dummy = Node(0)
        dummy.next = head

        while head:
            new_node = Node(head.val)
            new_node.next = head.next
            head.next = new_node
            head = new_node.next

        head = dummy.next
        while head:
            if head.random:
                head.next.random = head.random.next
            head = head.next.next
        
        head = dummy.next.next
        dummy.next = head
        while head:
            if head.next:
                head.next = head.next.next
            head = head.next
        
        return dummy.next
