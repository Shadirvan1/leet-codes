class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        first , blank = 0,0
        for i in moves:
            if i == "R":
                first += 1
            
            if i == "L":
                first -= 1
                
            if i == "_":
                blank += 1
                
        return abs(first) + blank


        # first , second = 0,0
        # l = moves.count("L")
        # r = moves.count("R")
        # b = moves.count("_")
        # return abs(l - r) + b

    




        """
        :type moves: str
        :rtype: int
        """
        