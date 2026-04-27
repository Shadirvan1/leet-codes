class Solution(object):
    def thirdMax(self, nums):
        nums = list(set(nums))

        nums.sort(reverse=True)
        print(len(nums))
        result = nums[2] if len(nums) >= 3 else max(nums)
        return result
        """
        :type nums: List[int]
        :rtype: int
        """
        