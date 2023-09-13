# Given a string, find the length of the longest substring T that contains at most k distinct characters.
#
# Example 1:
#
# Input: s = "eceba", k = 2
# Output: 3
# Explanation: T is "ece" which its length is 3.
# Example 2:
#
# Input: s = "aa", k = 1
# Output: 2
# Explanation: T is "aa" which its length is 2.

from collections import Counter


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        chars, ans, left = Counter(), 0, 0
        for right, c in enumerate(s):
            chars[c] += 1
            while left < len(s) and len(chars) > k:
                chars[s[left]] -= 1
                if chars[s[left]] == 0:
                    del chars[s[left]]
                left += 1

            ans = max(ans, right - left + 1)

        return ans


s = Solution()
print(s.lengthOfLongestSubstringKDistinct("eceba",2))
print(s.lengthOfLongestSubstringKDistinct("aa", 1))


