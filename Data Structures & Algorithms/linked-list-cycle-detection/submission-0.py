# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next or not head.next.next:
            return False

        slow = head
        fast = head.next.next

        while fast:
            if fast == slow:
                return True

            if not fast.next:
                break    

            fast = fast.next.next
            slow = slow.next    

        return False    