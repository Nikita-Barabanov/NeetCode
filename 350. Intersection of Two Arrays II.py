from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt1, cnt2 = Counter(nums1), Counter(nums2)
        ans = []
        for elem in cnt1:
            if elem in cnt2:
                ans.extend([elem] * min(cnt1[elem], cnt2[elem]))
        return ans

# class Solution:
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         return (Counter(nums1) & Counter(nums2)).elements()
