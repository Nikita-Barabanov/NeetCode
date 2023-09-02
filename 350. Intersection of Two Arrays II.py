from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def count(lst):
            counter = {}
            for elem in lst:
                counter[elem] = counter.get(elem, 0) + 1
            return counter

        counter1, counter2 = count(nums1), count(nums2)
        intersection = []
        for elem in counter1:
            if elem in counter2:
                intersection.extend([elem] * min(counter1[elem], counter2[elem]))

        return intersection
