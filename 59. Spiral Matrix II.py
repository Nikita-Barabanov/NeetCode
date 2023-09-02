from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y, d = 0, 0, 0
        i, v = directions[d]

        for idx in range(1, n*n + 1):
            matrix[x][y] = idx
            if x + i > n - 1 or x + i < 0 or y + v > n - 1 or y + v < 0 or matrix[x+i][y+v]:
                d = (d + 1) % 4
                i, v = directions[d]
            x, y = x + i, y + v

        return matrix
