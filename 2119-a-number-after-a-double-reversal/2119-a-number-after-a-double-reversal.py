class Solution(object):
    def isSameAfterReversals(self, num):
        # if num == 0:
        #     return True
        # return num % 10 != 0
        d = str(num)[::-1]
        ff = str(int(d))[::-1]
        if int(ff) == num:
            return True
        else:
            return False




      

        """
        :type num: int
        :rtype: bool
        """
        