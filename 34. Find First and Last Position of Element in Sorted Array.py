from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = bisect_left(nums, target), bisect_right(nums, target) - 1
        if left <= right:
            return [left, bisect_right(nums, target) - 1]
        return [-1, -1]
