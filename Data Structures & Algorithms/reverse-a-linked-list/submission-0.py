# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        fast = head.next
        slow = None

        while head:
            head.next = slow
            slow = head
            head = fast
            if fast:
               fast = fast.next

        return slow


        

            


        