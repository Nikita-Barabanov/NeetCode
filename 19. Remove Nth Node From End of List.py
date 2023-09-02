from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        root = ListNode(next=head)
        cur_node, del_node = root, root
        for _ in range(n - 1):
            cur_node = cur_node.next

        while cur_node:
            cur_node = cur_node.next
            del_node = del_node.next

        del_node.next = del_node.next.next

        return root.next