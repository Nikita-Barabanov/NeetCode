class Solution:
    def longestPalindrome(self, s: str) -> str:
        m_i, m_j, l = 0, 1, len(s)
        if l == 1:
            return s[m_i: m_j]
        dp = [[0 if j > i else 1 for j in range(l)] for i in range(l)]
        for i in range(l - 1, -1, -1):
            for j in range(l - 1, i, -1):
                v = 0
                if s[i] == s[j] and dp[i+1][j-1]:
                    v = 1
                    if j + 1 - i > m_j - m_i:
                        m_i, m_j = i, j + 1

                dp[i][j] = v

        return s[m_i: m_j]


s = Solution()
print(s.longestPalindrome("ccc"))
