class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        m, nums = 2, [1] * n
        nums[0] = nums[1] = 0

        while m * m < n:
            if nums[m]:
                nums[m * m: n: m] = [0] * ((n - m * m - 1) // m + 1)
            m += 1 if m == 2 else 2

        return sum(nums)
