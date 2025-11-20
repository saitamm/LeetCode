class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k % 2 == 0 or k % 5 == 0:
            return -1
        length = k-1
        div = 11
        small = 2
        while length != 0:
            if (div % k == 0):
                return small
            div = div *10 +1
            length -= 1
            small += 1
        return 1

        