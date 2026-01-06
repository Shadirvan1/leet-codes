class Solution(object):
    def findDuplicate(self, nums):
        nums.sort()
        for i in nums:
            if nums[i] == nums[i-1]:
                return nums[i]

    
                
        
            

        

            
        
        """
        :type nums: List[int]
        :rtype: int
        """
        