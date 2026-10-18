# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 0
        p = head
        while p:
            sz += 1
            p = p.next

        remove_index = sz - n
        if remove_index == 0:
            return head.next

        p = head
        for i in range(sz - 1):
            if (i + 1) == remove_index:
                p.next = p.next.next
                break
            p = p.next      
    
        return head            




        