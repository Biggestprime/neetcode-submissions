# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        return self.devide(lists, 0, len(lists) - 1)    

    def devide(self, lists, l, r):
        if l > r:
            return None

        if l == r:
            return lists[l]

        mid = l + (r - l) // 2
        left = self.devide(lists, l, mid)
        right = self.devide(lists, mid + 1, r)

        return self.merge(left, right)

    def merge(self, l1, l2):
        res = ListNode(0)
        cur = res

        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
            elif l1:
                cur.next = l1
                l1 = l1.next
            elif l2:
                cur.next = l2
                l2 = l2.next
            else:
                break

            cur = cur.next

        return res.next            




                
