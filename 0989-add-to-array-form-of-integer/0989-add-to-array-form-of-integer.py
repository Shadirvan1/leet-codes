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
        lst = []
        for i in d:
            lst.append(int(i))
        return lst
            

        