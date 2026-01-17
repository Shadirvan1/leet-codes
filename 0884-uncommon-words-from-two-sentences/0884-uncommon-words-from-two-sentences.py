class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        s1 = s1.split()
        s2 = s2.split()
        lst= s1+s2
        ll = []
        for i in lst:
            
            if lst.count(i) ==1:
                ll.append(i)
        return ll
            
        
        
        

        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        