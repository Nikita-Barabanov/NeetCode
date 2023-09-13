from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        a, b, cur_common, ans = set(), set(), 0, []
        for elem_a, elem_b in zip(A, B):
            if elem_a in b:
                cur_common += 1
            a.add(elem_a)
            if elem_b in a:
                cur_common += 1
            b.add(elem_b)
            ans.append(cur_common)

        return ans
