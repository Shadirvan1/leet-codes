class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s=0
        d=0
        ss = []
        for i in nums:
            if len(str(i)) == 1:
                s += i
            else:
                d += i
        if s != d:
            return True
        else:
            return False
