class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if "".join(sorted(t)) == "".join(sorted(s)):
            return True
        else:
            return False