# Given two strings s and t, determine if they are both one edit distance apart.
#
# Note:
# There are 3 possiblities to satisify one edit distance apart:
#
# Insert a character into s to get t
# Delete a character from s to get t
# Replace a character of s to get t
# Example 1:
#
# Input: s = "ab", t = "acb"
# Output: true
# Explanation: We can insert 'c' into s to get t.
# Example 2:
#
# Input: s = "cab", t = "ad"
# Output: false
# Explanation: We cannot get t from s by only one step.
# Example 3:
#
# Input: s = "1203", t = "1213"
# Output: true
# Explanation: We can replace '0' with '1' to get t.


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if m > n:
            return self.isOneEditDistance(t, s)

        for i in range(m):
            if s[i] != t[i]:
                if m == n:
                    return s[i + 1 :] == t[i + 1 :]
                return s[i:] == t[i + 1]

        return m + 1 == n


s = Solution()
print(s.isOneEditDistance("ab", "acb"))
print(s.isOneEditDistance("cab", "ad"))
print(s.isOneEditDistance("1203", "1213"))
print(s.isOneEditDistance("", ""))
print(s.isOneEditDistance("", "1"))
