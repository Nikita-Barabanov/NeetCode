def counter(s: str) -> dict:
    counter = {}
    for c in s:
        counter.setdefault(c, 0)
        counter[c] += 1

    return counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return counter(s) == counter(t)
