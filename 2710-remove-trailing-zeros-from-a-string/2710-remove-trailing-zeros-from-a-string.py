class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
        s = num[::-1]
        d = int(s)
        return str(d)[::-1]
        