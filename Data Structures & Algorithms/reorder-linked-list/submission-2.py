# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        self.recursive(head.next, head)      

# 1 2, 2 4, 3 6, 4 8, 5 10
# None 4 5 6 7
    def recursive(self, current: Optional[ListNode], head: Optional[ListNode]) -> ListNode:
        if not current:
            return head

        head = self.recursive(current.next, head)
        if not head:
            return None

        temp = None
        if head == current or head.next == current:
            current.next = None
        else:
            temp = head.next
            head.next = current
            current.next = temp
        # move first half forward    
        return temp                

# 1 2 3 4 5 6
# 1 6 2 3 4 5 6
#
#
#
#
    
    def reverse_itr(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            
            prev = curr
            curr = temp

        return prev    


    def reverse(self, current: Optional[ListNode], previous: Optional[ListNode]) -> Optional[ListNode]:
        if not current:
            return previous    

        head = self.reverse(current.next, current)
        current.next = previous    
        
        return head


