class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        u = set(s)
        t = s.count(s[0])
        for i in u:
            if s.count(i) == t:
                pass
            else:
                return False
        return True