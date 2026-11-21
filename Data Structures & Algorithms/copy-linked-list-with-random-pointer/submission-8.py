"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr = head
   
        while curr:
            copy = Node(curr.val, None, None)
            temp = Node(0, copy, curr.random)
            curr.random = temp
            curr = curr.next
        
        curr = head
        new_head = curr.random.next
        
        while curr:
            copy = curr.random.next
            random = curr.random.random

            if curr.next:
                copy.next = curr.next.random.next
            
            if random:
               copy.random = random.random.next

            curr = curr.next   

        return new_head