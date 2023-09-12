from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        ans = (right - left) * min(height[left], height[right])
        while left < right:
            cur = (right - left) * min(height[left], height[right])
            ans = max(cur, ans)
            if height[left] < height[right]:
                left += 1
            else:
                right += 1

        return ans