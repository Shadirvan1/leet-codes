class Solution(object):
    def canBeEqual(self, target, arr):
        target.sort()
        arr.sort()
        if arr == target:
            return True
        else:
            return False
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        