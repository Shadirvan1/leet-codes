class Solution(object):
    def singleNumber(self, nums):

        for i in nums:
            c = nums.count(i)
            print(c)
            if c < 3:
                return i
        """
        :type nums: List[int]
        :rtype: int
        """
        