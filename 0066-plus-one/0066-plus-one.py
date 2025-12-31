class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        d = int(''.join(map(str,digits)))
        f = d+1
        return [int(i) for i in str(f)]