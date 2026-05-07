class Solution(object):
    def subtractProductAndSum(self, n):
        s = 1
        d = 0
        for i in str(n):
            d+=int(i)
            s = s * int(i)
        return s - d
            
        """
        :type n: int
        :rtype: int
        """
        