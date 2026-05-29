class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d=[]
        for i in nums:
            s = 0
            for l in str(i):
                s += int(l)
            d.append(s)
            s = 0
        return min(d)
        