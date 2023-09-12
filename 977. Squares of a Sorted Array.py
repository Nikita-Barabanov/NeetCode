from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        i, ans = len(nums) - 1, [0 for _ in range(len(nums))]
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                ans[i] = nums[left] * nums[left]
                left += 1
            else:
                ans[i] = nums[right] * nums[right]
                right -= 1
            i -= 1

        return ans
