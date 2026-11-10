# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
     #split list to <= k chains
     #call reverse for each chain
     #collect chains
     #finally connect all chains using head and tail

        cnt = 1
        l, r = head, head
        chains = []
        while r:
            if cnt == k:
                temp = r.next
                r.next = None
                chains.append(self.reverse(l))
                l, r = temp, temp
                cnt = 1
                continue

            r = r.next  
            cnt += 1

        for i in range(len(chains) - 1):
            chains[i][1].next = chains[i + 1][0]

        if l:
            chains[len(chains) - 1][1].next = l

        return chains[0][0]                


    


    # return head, tail, if less than k return as it is
    def reverse(self, head):
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return (prev, head)

