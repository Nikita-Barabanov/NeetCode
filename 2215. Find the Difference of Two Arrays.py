from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1, set2 = set(nums1), set(nums2)
        ans1 = [elem for elem in set1 if elem not in set2]
        ans2 = [elem for elem in set2 if elem not in set1]

        return [ans1, ans2]