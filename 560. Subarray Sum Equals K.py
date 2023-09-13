from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix, ans, cur = {0: 1}, 0, 0
        for num in nums:
            cur += num
            ans += prefix.get(cur - k, 0)
            prefix[cur] = prefix.get(cur, 0) + 1

        return ans