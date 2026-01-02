class Solution(object):
    def reverseWords(self, s):
        r= s.split()
        l = r[::-1]
        m =""
        for i in l:
            m += i + " "
        return m.strip()

        """
        :type s: str
        :rtype: str
        """
        