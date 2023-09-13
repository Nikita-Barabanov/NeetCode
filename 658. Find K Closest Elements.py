from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        while left < len(arr) - k and \
        (abs(arr[left] - x) > abs(arr[left + k] - x) or arr[left] == arr[left + k]):
            left += 1

        return arr[left: left + k]

# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
#         left, right = 0, len(arr) - k
#         while left < right:
#             mid = (left + right) // 2
#             if x - arr[mid] > arr[mid + k] - x:
#                 left = mid + 1
#             else:
#                 right = mid
#
#         return arr[left: left + k]