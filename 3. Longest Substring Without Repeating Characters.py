class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars, max_substring = set(), 0
        left, right = 0, 0
        while right < len(s):
            if s[right] in chars:
                while s[left] != s[right]:
                    chars.remove(s[left])
                    left += 1
                chars.remove(s[left])
                left += 1
            chars.add(s[right])
            if right - left + 1 > max_substring:
                max_substring = right - left + 1
            right += 1

        return max_substring
