# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cnt = self.remove_recur(None, head, n)
        if cnt == n:
            head = head.next
        return head

    def remove_recur(self, prev: Optional[ListNode], current: Optional[ListNode], n: int) -> int:
        if not current:
            return 0                
    
        cnt = 1 if not current.next else self.remove_recur(current, current.next, n) + 1

        if cnt == n and prev and prev.next:
            prev.next = prev.next.next

        return cnt     





        