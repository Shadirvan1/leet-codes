class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        res = 0
        for j in jewels:
            for i in stones:
                if j == i:
                 res += 1
        return res
                

        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        