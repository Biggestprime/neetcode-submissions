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

        cnt = 0
        temp = head
        sec_head = None
        while temp:
            if cnt == math.ceil(list_size / 2) - 1:
                sec_head = temp.next
                temp.next = None
                break
            temp = temp.next
            cnt += 1

        sec_head = self.reverse(sec_head, None)
        
        curr = head
        while curr:
            temp = curr.next 
            curr.next = sec_head
            if sec_head:
               sec_head = sec_head.next
            if curr.next:   
               curr.next.next = temp
            curr = temp        



    def reverse(self, current: Optional[ListNode], previous: Optional[ListNode]) -> Optional[ListNode]:
        if not current:
            return previous    

        head = self.reverse(current.next, current)
        current.next = previous    
        
        return head


