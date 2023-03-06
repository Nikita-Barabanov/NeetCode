from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        flips, max_beauty = k, 0
        left, right = 0, 0

        while right < len(nums):
            if not nums[right]:
                if flips:
                    flips, left = flips - 1, left - 1
                elif nums[left]:
                    while nums[left]:
                        left += 1

                left += 1

            max_beauty = max(max_beauty, right - left + 1)
            right += 1

        return max_beauty


