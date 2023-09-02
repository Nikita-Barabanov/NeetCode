class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        p = [0] * m
        i, j = 1, 0
        while i < m:
            if needle[i] == needle[j]:
                p[i] = j + 1
                i, j = i + 1, j + 1
            else:
                if j == 0:
                    p[i] = 0
                    i += 1
                else:
                    j = p[j - 1]

        i, j = 0, 0
        while i < n:
            if haystack[i] == needle[j]:
                i, j = i + 1, j + 1
                if j == m:
                    return i - m
            else:
                if j > 0:
                    j = p[j - 1]
                else:
                    i += 1

        return -1