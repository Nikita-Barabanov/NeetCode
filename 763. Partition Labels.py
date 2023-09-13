from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        positions = {}
        for idx, c in enumerate(s):
            if c not in positions:
                positions[c] = [idx, idx + 1]
            else:
                positions[c][1] = idx + 1

        segments, ans = list(positions.values()), []
        cur = segments[0]
        for segment in segments:
            if segment[0] < cur[1]:
                cur[1] = max(cur[1], segment[1])
            else:
                ans.append(cur)
                cur = [segment[0], segment[1]]
        ans.append(cur)

        return [segment[1] - segment[0] for segment in ans]
    