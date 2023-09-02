from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur_node = root_node = ListNode()
        add = 0
        while l1 or l2:
            s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + add
            val, add = s % 10, s // 10
            cur_node.next = ListNode(val)
            cur_node = cur_node.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if add:
            cur_node.next = ListNode(1)

        return root_node.next


s = Solution()
ans = s.addTwoNumbers(ListNode(3, ListNode(2, ListNode(1))), ListNode(4, ListNode(3, ListNode(2, ListNode(1)))))
while ans:
    print(ans.val)
    ans = ans.next
