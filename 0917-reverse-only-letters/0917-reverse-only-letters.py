class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = []

        for i in s:
            if i.isalpha():
                l.insert(0,i)
        for i in range(len(s)): 
            if not s[i].isalpha():
                l.insert(i,s[i])

        return "".join(l)
