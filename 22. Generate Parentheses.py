from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dfs, answer = [(0, 0, "")], []
        while dfs:
            open, close, cur_str = dfs.pop()
            if len(cur_str) == 2*n:
                answer.append(cur_str)
            if open < n:
                dfs.append((open + 1, close, cur_str + "("))
            if close < open:
                dfs.append((open, close + 1, cur_str + ")"))

        return answer

s = Solution()
print(s.generateParenthesis(8))