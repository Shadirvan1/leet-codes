class Solution(object):
    def heightChecker(self, heights):
        d = sorted(heights)
        s = 0
        if d == heights:
            return 0
        for i in range(len(heights)):
            if d[i] != heights[i]:
                s += 1
            else:
                pass
        return s



        """
        :type heights: List[int]
        :rtype: int
        """
        