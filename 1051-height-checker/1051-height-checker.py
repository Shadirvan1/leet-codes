class Solution(object):
    def heightChecker(self, heights):
        s = 0
        d = sorted(heights)
        print(d)
        if d == heights:
            return 0
        for i in range(len(heights)):
            print(i)
            if d[i] != heights[i]:
                s += 1
            else:
                pass
        return s



        """
        :type heights: List[int]
        :rtype: int
        """
        