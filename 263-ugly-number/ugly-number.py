class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if (n <= 0):
            return False
        if (n == 1 or n == 2 or n == 3 or n == 5):
            return (True)
        div = 2
        diviseurs = []
        d = [[2], [2, 3],[2, 5], [2, 3, 5], [3],[3, 5], [5] ]
        for div in range(2, int(math.sqrt(n)) + 1):
            if (n % div == 0):
                print(div)
                if div == 2 or div == 3 or div ==  5:
                    diviseurs.append(div)
                if div % 2 != 0 and div % 3 != 0 and div % 5 != 0:
                    diviseurs.append(div)
                if div != n // div and ( n // div) % 2 != 0 and ( n // div) % 3 != 0 and ( n // div) % 5 != 0:
                        diviseurs.append(n // div)
        print(diviseurs)
        return (diviseurs in d )
