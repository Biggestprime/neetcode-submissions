# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        queue = deque()

        for list in lists:
            queue.append(list)

        while len(queue) > 1:
            first = queue.popleft()
            second = queue.popleft()
            merged = self.merge(first, second)
            queue.append(merged)

        return queue.popleft()



    def merge(self, l1, l2):

        head = ListNode(0)
        curr = head
        while True:
            if l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
            elif l1:
                curr.next = l1
                l1 = l1.next
            elif l2:
                curr.next = l2
                l2 = l2.next
            else:
                break                

            curr = curr.next    

        return head.next


