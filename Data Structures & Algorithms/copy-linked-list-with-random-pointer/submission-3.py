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
        oldToCopy = collections.defaultdict(lambda: Node(0))
        oldToCopy[None] = None

        current = head

        while current:
            copy = oldToCopy[current]
            copy.val = current.val

            copy.next = oldToCopy[current.next]
            copy.random = oldToCopy[current.random]

            current = current.next

        return oldToCopy[head]        
        



