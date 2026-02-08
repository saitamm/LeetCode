class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n <= 2):
            return 0
        isPrime = [True for i in range(0,n)]
        isPrime[0] = False
        isPrime[1] = False
        for i in range(2, int(math.sqrt(n))+1):
            if (isPrime[i]):
                for j in range(i*i, n, i):
                    isPrime[j] = False
        return sum(isPrime)