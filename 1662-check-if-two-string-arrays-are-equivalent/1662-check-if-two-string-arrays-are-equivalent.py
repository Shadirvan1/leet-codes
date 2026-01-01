class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        r = ""
        r1 = ""
        for i in word1:
            r += i
        for j in word2:
            r1 += j 
        if r == r1:
            return True
        else:
            return False

        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        