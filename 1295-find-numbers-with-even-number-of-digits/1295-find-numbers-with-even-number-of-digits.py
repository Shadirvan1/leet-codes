class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 0
        for i, value in enumerate(nums):
            if len(str(value))%2==0:
                c += 1
        return c
