from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = sum(nums[:3])
        for i, x in enumerate(nums):
            j, k = i + 1, len(nums) - 1
            while j < k:
                s = x + nums[j] + nums[k]
                if s < target:
                    j += 1
                elif s > target:
                    k -= 1
                else:
                    return s

                if abs(s - target) < abs(ans - target):
                    ans = s

        return ans