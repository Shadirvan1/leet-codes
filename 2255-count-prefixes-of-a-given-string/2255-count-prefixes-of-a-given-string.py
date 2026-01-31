class Solution(object):
    def countPrefixes(self, words, s):
        l=0
        for i in words:
            if s.startswith(i):
                l+=1
        return l
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        