class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        ans = -1

        for num in nums:
            if num > 0 and -num in num_set:
                ans = max(ans, num)

        return ans
        