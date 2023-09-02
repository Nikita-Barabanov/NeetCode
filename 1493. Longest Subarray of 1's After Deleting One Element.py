from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeroes, left, ans = 0, 0, 0
        for right in range(len(nums)):
            if not nums[right]:
                zeroes += 1
            while zeroes > 1:
                if not nums[left]:
                    zeroes -= 1
                left += 1

            ans = max(ans, right - left + 1 - zeroes)

        return ans - 1 if ans == len(nums) else ans