from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        pre, cur, new_head = None, head, None
        while cur:
            cur, pre = cur.next, cur
            pre.next = new_head
            new_head = pre


        return new_head
