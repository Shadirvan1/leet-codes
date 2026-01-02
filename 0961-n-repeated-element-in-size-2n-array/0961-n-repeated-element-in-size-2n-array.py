class Solution(object):
    def repeatedNTimes(self, nums):
        
        for i in nums:
            n = nums.count(i)
            if n >= 2:
                return i
            
            

        """
        :type nums: List[int]
        :rtype: int
        """
        