class Solution(object):
    def findGCD(self, nums):
        m = min(nums)
        ma = max(nums)
        res = 0
        for i in range(1,ma+1):
            if m%i==0 and ma%i==0:
                res = i
        return res


        """
        :type nums: List[int]
        :rtype: int
        """
        