class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for i in words:
            d = i[::-1]
            if d==i:
                return i
        return ""