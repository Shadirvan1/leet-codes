class Solution(object):
    def isHappy(self, n):
        seen = set()

        while n != 1:

            if n in seen:
                return False

            seen.add(n)

            s = 0

            for i in str(n):
                d = int(i) * int(i)
                s += d

            n = s

        return True