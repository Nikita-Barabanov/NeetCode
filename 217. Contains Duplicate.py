from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        for elem in nums:
            if elem in unique:
                return True
            unique.add(elem)
        return False
