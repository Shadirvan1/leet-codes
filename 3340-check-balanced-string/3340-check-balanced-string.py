class Solution(object):
    def isBalanced(self, num):
        """
        :type num: str
        :rtype: bool
        """
        s = 0
        d = 0
        for v,i in enumerate(num):
            print(i)
            if v % 2 == 0:
                s += int(i)
            else:
                d += int(i)
        if s == d:
            return True
        return False
