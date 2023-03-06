from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        left, right = 0, 0

        while right < len(chars):
            cur_char, cnt = chars[right], 1

            while chars[right] == (chars[right + 1] if right < len(chars) - 1 else ""):
                right += 1
                cnt += 1

            chars[left] = cur_char
            if cnt > 1:
                for c in str(cnt):
                    left += 1
                    chars[left] = c

            left += 1
            right += 1
        return left


s = Solution()
print(s.compress(["a","a","a","b","b","a","a"]))