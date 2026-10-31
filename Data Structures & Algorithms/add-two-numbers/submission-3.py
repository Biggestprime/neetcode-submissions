# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.addTwoNumbers_rec(l1, l2, 0)

    def addTwoNumbers_rec(self, l1: Optional[ListNode], l2: Optional[ListNode], rem: int) -> Optional[ListNode]:
        if not l1 and not l2:
            if rem == 0:
                return None
            return ListNode(rem)

        sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + rem
        new_node = ListNode(sum % 10)
        next = self.addTwoNumbers_rec(l1.next if l1 else None, l2.next if l2 else None, sum // 10)
        new_node.next = next
        return new_node

        



        
 

