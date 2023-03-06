from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        start, end, cur_val, ranges = 0, 0, nums[0] - 1, []
        while end < len(nums):
            cur_val += 1
            if nums[end] != cur_val:
                ranges.append(f"{nums[start]}" + (f"->{nums[end-1]}" if end-1 != start else ""))
                start, cur_val = end, nums[end]
            end += 1

        if start != end:
            ranges.append(f"{nums[start]}" + (f"->{nums[end-1]}" if end-1 != start else ""))

        return ranges
