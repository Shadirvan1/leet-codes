class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        sum = str(x)
        l = 0 
        for i in sum:
            l += int(i)
        if x%l == 0:
        
            return l
        else:
            return -1



        