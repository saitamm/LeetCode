class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        number  = x
        result = 0
        if (x <0):
            return (False)
        while number != 0 :
            result = result * 10 + (number % 10 )
            number = number / 10
        return result == x 
