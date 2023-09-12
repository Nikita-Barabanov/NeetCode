# Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points.
#
# Example 1: Given points = [[1,1],[-1,1]], return true.
#
# Example 2: Given points = [[1,1],[-1,-1]], return false.
#
# Follow up: Could you do better than O(n2)?
#
# Hint:
#
# Find the smallest and largest x-value for all points. If there is a line then it should be at y = (minX + maxX) / 2.
# For each point, make sure that it has a reflected point in the opposite side.

from typing import List

class Solution:
    def isReflected(self, points: List) -> bool:
        points = set(tuple(point) for point in points)
        min_p, max_p = min(points), max(points)
        reflect_x = (min_p[0] + max_p[0])
        for point in points:
            if (reflect_x - point[0], point[1]) not in points:
                return False

        return True


s = Solution()
print(s.isReflected([[1,1],[-1,1]]))
print(s.isReflected([[1,1],[-1,-1]]))