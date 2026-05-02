class Solution(object):
    def maxRotateFunction(self, nums):
        n = len(nums)
        total_sum = sum(nums)
        f = sum(i * nums[i] for i in range(n))
        res = f
        for i in range(1, n):
            f = f + total_sum - n * nums[n - i]
            res = max(res, f)
        return res