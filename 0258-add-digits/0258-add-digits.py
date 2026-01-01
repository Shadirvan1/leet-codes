class Solution(object):
    def addDigits(self, num):
        i = True
        vv = num
        while i:

            n = list(str(vv))
            v = [int(i) for i in n]
            vv = sum(v)
            if vv <= 9:
                i = False


        return vv
        # while i:
        #     for n in str(num):
        #         sum = int(n)


        #     if  sum <= 9:
        #         i = False



        """
        :type num: int
        :rtype: int
        """
        