from typing import List

# [4,2,0,3,2,5]
#      #
# #    #
# #  # #
# ## ###
# ## ###
# 012345


class Solution:
    def trap(self, height: List[int]) -> int:
        ans, stack = 0, []
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                pop_i = stack.pop()
                if not stack:
                    break
                ans += (i - stack[-1] - 1) * (min(height[i], height[stack[-1]]) - height[pop_i])
            stack.append(i)
        return ans

s = Solution()
print(s.trap([4,2,0,3,2,5]))


