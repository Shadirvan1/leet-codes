class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = set(nums)
        if len(d) == len(nums):
            return False
        else:
            return True