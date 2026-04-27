class Solution(object):
    def moveZeroes(self, nums):
        s = nums.count(0)
        nums[:] = [x for x in nums if x != 0]
        nums.extend([0] * s)
        
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        