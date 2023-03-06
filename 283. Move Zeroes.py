from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_cnt = 0
        for idx in range(len(nums)):
            if nums[idx] == 0:
                zero_cnt += 1
            else:
                nums[idx - zero_cnt] = nums[idx]

        for idx in range(len(nums) - zero_cnt, len(nums)):
            nums[idx] = 0
