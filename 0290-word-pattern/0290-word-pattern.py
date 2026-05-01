class Solution(object):
    def wordPattern(self, pattern, s):

        word = s.split()
        if len(word) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern.index(pattern[i]) != word.index(word[i]):
                return False
        return True
        
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        
        
        
        

        