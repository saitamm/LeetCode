class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        x = int(math.sqrt(num))
        if x*x == num:
            return True
        return(False)