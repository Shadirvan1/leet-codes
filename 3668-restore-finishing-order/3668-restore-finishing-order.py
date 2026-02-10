class Solution(object):
    def recoverOrder(self, order, friends):
        c = []
        for i in order:
            if i in friends:
                c.append(i)
        return c
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        