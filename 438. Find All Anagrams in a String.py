from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        if n < m:
            return []

        s_cnt, p_cnt, ans = Counter(s[:m]), Counter(p), []
        if s_cnt == p_cnt:
            ans.append(0)
        for i in range(n - m):
            s_cnt[s[i + m]] += 1
            s_cnt[s[i]] -= 1
            if s_cnt == p_cnt:
                ans.append(i + 1)

        return ans