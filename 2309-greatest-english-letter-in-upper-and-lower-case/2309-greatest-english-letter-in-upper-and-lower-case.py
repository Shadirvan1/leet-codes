class Solution(object):
    def greatestLetter(self, s):
        l = list(s)
        l.sort()
        d = ""
        print(l)
        for i in range(len(l)-1,-1,-1):
            print(i)
            if l[i].upper() in l and l[i].lower() in l:
                return str(l[i].upper())
            else:
                pass
        return d

        """
        :type s: str
        :rtype: str
        """
        