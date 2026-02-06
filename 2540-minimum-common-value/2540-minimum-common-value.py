class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
    


        # for i in l:
        #     if l.count(i) >= 2:
        #         cc.append(i)
        res = set(nums1) & set(nums2)
        print(list(res))
        if len(res) == 0:
            return -1
        return min(list(res))
        

