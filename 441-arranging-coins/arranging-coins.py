class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int

        """
        low = 1
        high = n
        while True:
            mid = (low + high)/2
            Sum = mid*(mid+1)/2
            if Sum > n :
                high = mid
            elif Sum <= n:
                low = mid 
                S = (mid+1)*(mid+2)/2
                if S > n:
                    return mid
        return(-1)           
