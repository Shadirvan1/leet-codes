class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
       
        d =[x for x in s if x.isalpha() or x.isdigit()]
        print(d)
        dd = d[::-1]
        print(dd)
        if d == dd:
            return True
        else:
            return False
        """
        :type s: str
        :rtype: bool
        """
        