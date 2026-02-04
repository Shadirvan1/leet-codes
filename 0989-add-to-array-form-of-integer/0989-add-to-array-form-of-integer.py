class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        l = ""
        for i in num:
            l += str(i)
        d =str(int(l) + k)
        lst = [int(i) for i in d]
        return lst
            

        