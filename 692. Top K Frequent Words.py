from heapq import heappop, heappush
from typing import List
from collections import Counter


class Pair:
    def __init__(self, word, frequency):
        self.word, self.frequency = word, frequency

    def __lt__(self, other):
        return self.frequency < other.frequency or \
        (self.frequency == other.frequency and self.word > other.word)


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        pairs, heap = Counter(words), []
        for word, freq in pairs.items():
            heappush(heap, Pair(word, freq))
            if len(heap) > k:
                heappop(heap)

        return [pair.word for pair in sorted(heap, reverse=True)]