# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = self.recursive(head, n)

        if count == n:
            return head.next
        else:
            return head    

    def recursive(self, current: Optional[ListNode], n: int) -> int:
        if not current.next:
            return 1
        
        count = self.recursive(current.next, n)
        
        if count == n:
            current.next = current.next.next
        
        return count + 1    