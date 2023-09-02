from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

        hash_table, ans = {0: 1}, 0
        for s in nums:
            ans += hash_table.get(s % k, 0)
            hash_table[s % k] = hash_table.get(s % k, 0) + 1

        return ans