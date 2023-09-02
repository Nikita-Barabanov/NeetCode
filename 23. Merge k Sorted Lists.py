from typing import List, Optional
from heapq import heapify, heappop, heappush
from functools import cmp_to_key


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # def __lt__(self, other):
    #     return self.val < other.val
    #
    # def __eq__(self, other):
    #     return self.val == other.val
    #
    # def __str__(self):
    #     ans = []
    #     cur = self
    #     while cur:
    #         ans.append(cur.val)
    #         cur = cur.next
    #
    #     return str(ans)


def new_heapify(data, cmp):
    s = list(map(cmp_to_key(cmp), data))
    heapify(s)
    return s


def new_heappop(data):
    return heappop(data).obj


def new_heappush(data, cmp, item):
    heappush(data, cmp_to_key(cmp)(item))


def cmp(x, y):
    return x.val-y.val



class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda self, other: self.val < other.val
        ListNode.__eq__ = lambda self, other: self.val == other.val
        cur_node = root_node = ListNode(val=-1)

        lists = [list for list in lists if list]
        heapify(lists)

        while lists:
            pop_node = heappop(lists)
            cur_node.next = pop_node
            cur_node = pop_node
            if pop_node and pop_node.next:
                heappush(lists, pop_node.next)

        return root_node.next

s = Solution()
_ = s.mergeKLists([None, None])
while _:
    print(_.val)
    _ = _.next