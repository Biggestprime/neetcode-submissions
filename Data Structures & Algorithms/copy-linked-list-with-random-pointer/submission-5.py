"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

        3
        7           null
        4   5 
        5 3 null 3
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        current = head
        while current:
            copy = Node(current.val, current.next, current.random)
            current.next = copy
            current = current.next.next

        
        current = head.next
        while current:
            if current.random:
               current.random = current.random.next

            current = current.next.next if current.next else None

        head_copy = head.next
        current = head
        while current:
            current_next = current.next.next if current.next else None
            copy = current.next
            copy_next = current.next.next.next if current.next and current.next.next else None

            current.next = current_next
            copy.next = copy_next
            
            current = current_next

        return head_copy    




