class Solution(object):
    def lengthOfLastWord(self, s):
        data = s.split()
        n = len(data)
        f = data[n-1]
        return len(str(f))

        """
        :type s: str
        :rtype: int
        """
        