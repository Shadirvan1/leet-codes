class Solution(object):
    def mostWordsFound(self, sentences):
        out = 0
        for n in sentences:
            l = n.split(' ')
            nn = len(l)
            if out < nn:
                out = nn
        return out


        """
        :type sentences: List[str]
        :rtype: int
        """
        