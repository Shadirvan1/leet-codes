class Solution(object):
    def moveZeroes(self, nums):
        s = nums.count(0)
        print(s)
        nums[:] = [x for x in nums if x != 0]
        print(nums)
        nums.extend([0] * s)
        print(nums)
        
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        