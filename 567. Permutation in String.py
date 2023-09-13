from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt1, cnt2 = Counter(s1), Counter(s2[:len(s1)])
        if cnt1 == cnt2:
            return True

        for i in range(len(s2) - len(s1)):
            cnt2[s2[i]] -= 1
            cnt2[s2[i + len(s1)]] += 1
            if cnt1 == cnt2:
                return True

        return False