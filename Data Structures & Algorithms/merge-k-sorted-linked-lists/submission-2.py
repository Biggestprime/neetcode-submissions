# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# l1 l2 l3 l4
# n + n log n
# n
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        all_nodes = list()
        current = None
        for index in range(len(lists)):
            current = lists[index]
            while current:
                all_nodes.append(current)
                current = current.next
        srtd = sorted(all_nodes, key = lambda node: node.val)

        for i in range(len(srtd) - 1):
            srtd[i].next = srtd[i + 1]

        return srtd[0] if srtd else None    

