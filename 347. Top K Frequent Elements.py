from typing import List


def counter(a) -> dict:
    counter = {}
    for elem in a:
        counter[elem] = counter.get(elem, 0) + 1

    return counter



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = [[] for _ in range(len(nums) + 1)]
        counts = counter(nums)
        for num, freq in counts.items():
            freqs[freq].append(num)
        most, c = [], 0
        for i in range(len(nums), -1, -1):
            for elem in freqs[i]:
                most.append(elem)
                if len(most) >= k:
                    return most


s = Solution()
print(s.topKFrequent([1], 1))
