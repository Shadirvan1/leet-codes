class Solution(object):
    def firstUniqChar(self, s):
        l = ""
        for i in s:
            if i in l:
                continue
            if s.count(i) == 1:
                return s.index(i)
            else:
                l += i
                pass
        return -1
        

        """
        :type s: str
        :rtype: int
        """
        