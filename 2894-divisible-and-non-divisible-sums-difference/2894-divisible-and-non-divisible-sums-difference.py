class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        s,d =0,0
        for i in range(1,n+1):
            if i % m == 0:
                s += i
            else:
                d += i
        return d - s 
            