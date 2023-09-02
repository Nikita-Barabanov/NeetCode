from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur_node = root_node = ListNode(-1)

        while list1 and list2:
            if list1.val < list2.val:
                cur_node.next, list1 = list1, list1.next
            else:
                cur_node.next, list2 = list2, list2.next
            cur_node = cur_node.next

        for end in list1, list2:
            if end:
                cur_node.next = end

        return root_node.next

