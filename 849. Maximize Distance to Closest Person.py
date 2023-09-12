from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        div, ans, cur = 1, 0, 0
        for seat in seats:
            if seat:
                ans = max(ans, cur // div + cur % div)
                div, cur = 2, 0
            else:
                cur += 1

        if not seats[-1]:
            ans = max(ans, cur)

        return ans