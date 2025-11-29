# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        first = -1
        if n == 1:
             return (n)
        while start <= n :
            bad = (start + n )/2
            if isBadVersion(bad) == False :
                start = bad +1
            elif isBadVersion(bad) == True:
                n = bad -1
                first = bad
        return first