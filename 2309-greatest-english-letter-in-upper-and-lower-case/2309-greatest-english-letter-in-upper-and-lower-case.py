class Solution(object):
    def greatestLetter(self, s):
        l = list(s)
        l.sort(reverse=True)
        d = ""
        print(l)
        for i in l:
            if i.upper() in l and i.lower() in l:
                return str(i.upper())
            else:
                pass
        return d

        """
        :type s: str
        :rtype: str
        """
        