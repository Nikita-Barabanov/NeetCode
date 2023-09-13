# Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.
#
# Example 1:
#
# Input: [1,0,1,1,0]
# Output: 4
# Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
#     After flipping, the maximum number of consecutive 1s is 4.
# Note:
#
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000
# Follow up: What if the input numbers come in one by one as an infinite stream? In other words, you can't store all
# numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently?

from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left, zero_index, ans = 0, -1, 0
        for right, num in enumerate(nums):
            if not num:
                left = zero_index + 1
                zero_index = right

            ans = max(ans, right - left + 1)

        return ans


s = Solution()
print(s.findMaxConsecutiveOnes([1,0,1,1,0]))
print(s.findMaxConsecutiveOnes([1,1,1,1,0]))
print(s.findMaxConsecutiveOnes([0,0,0]))
print(s.findMaxConsecutiveOnes([1,1,1]))
print(s.findMaxConsecutiveOnes([1]))
print(s.findMaxConsecutiveOnes([0]))
print(s.findMaxConsecutiveOnes([]))