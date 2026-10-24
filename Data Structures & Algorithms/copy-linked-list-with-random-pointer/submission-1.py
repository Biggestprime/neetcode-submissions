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
        self.dfs(head, dict)
        return dict[head]

    def dfs(self, current: Optional[Node], dict: dict[Node, Node]) -> None:
        if not current:
            return

        copy = Node(current.val, None, None)
        dict[current] = copy
        self.dfs(current.next, dict)

        next = dict[current.next] if current.next else None
        random = dict[current.random] if current.random else None
        copy.next = next
        copy.random = random
        



