class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        d = []
        for i in arr:
            
            if i % 2 != 0:
                
                d.append(i)
                if 3 == len(d):
                    return True
                
            else:
                
                d[:] = []
        return False