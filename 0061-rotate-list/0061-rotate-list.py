# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None:
            return None
        q = deque()
        ans = head
        while head:
            q.append(head.val)
            head = head.next
        k = k%len(q)
        fin = ans
        q.rotate(k)
        for i in range(len(q)):
            ans.val = q[i]
            if i!= len(q)-1:
                ans.next = ListNode()
            ans = ans.next

        return fin