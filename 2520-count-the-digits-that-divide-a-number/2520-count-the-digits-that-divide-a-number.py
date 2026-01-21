class Solution(object):
    def countDigits(self, num):
        n = str(num)
        c = 0
        for i in n:
            print(i)
            if num % int(i)== 0:
                c+=1
            else:
                c
        return c

        """
        :type num: int
        :rtype: int
        """
        