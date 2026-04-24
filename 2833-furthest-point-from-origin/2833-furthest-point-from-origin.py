class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        first , second = 0,0
        l = moves.count("L")
        r = moves.count("R")
        b = moves.count("_")
        return abs(l - r) + b

    




        """
        :type moves: str
        :rtype: int
        """
        