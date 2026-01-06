class Solution(object):
    def singleNumber(self, nums):
        n = 0
        for i in nums:
            f = nums.count(i)
            if f == 1:
                return i



        """
        :type nums: List[int]
        :rtype: int
        """
        