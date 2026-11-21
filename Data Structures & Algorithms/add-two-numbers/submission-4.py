# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rem = 0

        head = None
        curr = head
        while l1 or l2 or rem != 0:
            sum = rem + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            new_node = ListNode(sum % 10)
            rem = sum // 10
            
            if not head:
                head = new_node
                curr = head
            else:
                curr.next = new_node
                curr = new_node
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next        
            
        return head