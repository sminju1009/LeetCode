# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heapify, heappush, heappop

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [(li.val, idx) for idx, li in enumerate(lists) if li]
        heapify(heap)

        dummy = curr = ListNode(-1)
        while heap:
            val, idx = heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next

            lists[idx] = lists[idx].next
            if lists[idx]:
                heappush(heap, (lists[idx].val, idx))
        return dummy.next