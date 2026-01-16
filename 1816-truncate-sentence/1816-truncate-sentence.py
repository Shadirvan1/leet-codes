class Solution(object):
    def truncateSentence(self, s, k):
        ll = s.split()
        l =""
        for i in range(k):
            l += ll[i] + ' '
        return l.strip()

        """
        :type s: str
        :type k: int
        :rtype: str
        """
        