# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        list_size = 0
        temp = head
        while temp:
            list_size+=1
            temp = temp.next

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        sec_head = slow
        sec_head = self.reverse_itr(sec_head)

        curr = head
        while curr:
            temp = curr.next 
            curr.next = sec_head
            if sec_head:
               sec_head = sec_head.next
            if curr.next:   
               curr.next.next = temp
            curr = temp        

# 1 2, 2 4, 3 6, 4 8, 5 10
# None 4 5 6 7
    
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


