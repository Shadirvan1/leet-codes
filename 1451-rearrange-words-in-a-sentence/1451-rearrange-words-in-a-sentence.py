class Solution(object):
    def arrangeWords(self, text):
        sp = text.split()
        sp.sort(key=len)
        res = " ".join(sp)
        res.lower()
        return res.capitalize()

        """
        :type text: str
        :rtype: str
        """
        