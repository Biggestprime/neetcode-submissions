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
            copy = Node(current.val, None, None)
            temp = Node(0, copy, current.random)
            current.random = temp
            current = current.next

        current = head
        while current:
            copy = current.random.next
            random = current.random.random
            
            if current.next:
               copy.next = current.next.random.next

            if random:   
                copy.random = random.random.next

            current = current.next

        head_copy = head.random.next  
        current = head
        while current:
            current.random = current.random.random
            current = current.next

        return head_copy    




#next -- known
#random -- known

# n1 - n2 - n3 - n4
# c1 - c2 - c3 - c4

#next -- known
#random -- Empty Node random, random.next = copy of current node, random.random = random node


