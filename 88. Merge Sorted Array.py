from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums = nums1[:m]
        i, j = 0, 0
        for c in range(m + n):
            n1, n2 = nums[i] if i < m else None, nums2[j] if j < n else None
            print(n1, n2)
            if n1 is not None and (n2 is None or n1 <= n2):
                nums1[c], i = n1, i + 1
            else:
                nums1[c], j = n2, j + 1


s = Solution()
n = [-1,0,0,3,3,3,0,0,0]
s.merge(n, 6, [1,2,2], 3)
print(n)