from typing import List


# Slow
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         ans = set()
#         for idx, x in enumerate(nums):
#             seen = set()
#             for y in nums[:idx]:
#                 if (z := - (x + y)) in seen:
#                     triplet = [x, y, z]
#                     triplet.sort()
#                     triplet = tuple(triplet)
#                     ans.add(triplet)
#                 seen.add(y)
#
#         return list(list(_) for _ in ans)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i, x in enumerate(nums):
            if not (i > 0 and nums[i] == nums[i - 1]):
                j, k = i + 1, len(nums) - 1
                while j < k:
                    s = x + nums[j] + nums[k]
                    if s > 0:
                        k -= 1
                    elif s < 0:
                        j += 1
                    else:
                        ans.append([x, nums[j], nums[k]])
                        j += 1
                        while nums[j - 1] == nums[j]:
                            j += 1

        return ans



s = Solution()
print(s.threeSum([0, 0, 0]))
