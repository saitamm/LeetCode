class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k % 2 == 0 or k % 5 == 0:
            return -1
        div = 0
        for length in range(1, k+1):
            div = (div *10 +1) % k
            if div == 0:
                return length
        return -1

        