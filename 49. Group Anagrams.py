from typing import List


def counter(s: str) -> dict:
    counter = {}
    for c in s:
        counter.setdefault(c, 0)
        counter[c] += 1

    return counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            rle = "".join(f"{c}{num if num > 1 else ''}" for c, num in sorted(counter(s).items()))
            anagrams.setdefault(rle, [])
            anagrams[rle].append(s)

        return list(anagrams.values())
