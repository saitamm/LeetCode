class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        pivot = -1
        sumleft = 1
        sumright = n
        while left <= right:
            if (left == right and sumleft == sumright):
                pivot = left
            if (sumleft <= sumright):
                left += 1
                sumleft += left
            if (sumright < sumleft):
                right-=1
                sumright += right
        return pivot
