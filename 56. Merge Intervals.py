from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans, cur = [], intervals[0]

        for left, right in intervals:
            if left <= cur[1]:
                cur[1] = max(right, cur[1])
            else:
                ans.append(cur)
                cur = [left, right]
        ans.append(cur)

        return ans


s = Solution()
print(s.merge([[1,3],[1,2], [1, 1]]))