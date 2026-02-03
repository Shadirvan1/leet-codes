class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=""
        j = []
        for i in nums:
            d = str(i)
            l += d
            print(l)
        for i in l:
            print(i)
            j.append(int(i))
        return j


        print(d)
        