class Solution(object):
    def numOfWays(self, n):
        MOD = 10**9 + 7
        two = 6   
        three = 6 

        for _ in range(2, n + 1):
            new_two = (two * 3 + three * 2) % MOD
            new_three = (two * 2 + three * 2) % MOD

            two, three = new_two, new_three

        return (two + three) % MOD


        """
        :type n: int
        :rtype: int
        """
        