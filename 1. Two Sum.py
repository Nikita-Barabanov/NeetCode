from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        validx = {}
        for idx, num in enumerate(nums):
            if target - num in validx.keys():
                return [validx[target - num], idx]
            validx[num] = idx
