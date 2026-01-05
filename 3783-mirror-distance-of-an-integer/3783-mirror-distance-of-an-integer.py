class Solution(object):
    def mirrorDistance(self, n):
        d  = str(n)
        j = d[::-1]
        e = int(j)
        print(e)
        f = e - n
        return abs(f)

        
        """
        :type n: int
        :rtype: int
        """
        