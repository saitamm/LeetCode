class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k % 2 == 0 or k % 5 == 0:
            return -1
        length = k
        div = 1
        for i in range(1, k):
            div = div * 10 + 1
        small = 1
        while div != 1:
            if (div % k == 0):
                small = length
            div = div / 10
            length -= 1
        return small

        