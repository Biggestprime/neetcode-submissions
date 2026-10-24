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

        dict = {}
        
        pointer = head
        while pointer:
            copy = Node(pointer.val)
            dict[pointer] = copy
            pointer = pointer.next

        pointer = head
        while  pointer:
            copy = dict[pointer]
            copy.next = dict[pointer.next] if pointer.next else None
            copy.random = dict[pointer.random] if pointer.random else None
            pointer = pointer.next

        return dict[head]       
        



