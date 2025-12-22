class Solution(object):
    def lengthOfLastWord(self, s):
        ss = s.strip().split(' ')
        
        l = len(ss) - 1
        last = ss[l]
        return len(last)
        
        """
        :type s: str
        :rtype: int
        """
        