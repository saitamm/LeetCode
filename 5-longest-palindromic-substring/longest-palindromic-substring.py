class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxlength = 1
        start = 0
        end = 1
        for i in range(0, len(s)):
            left = i
            right = i + 1
            while left >= 0 and s[left] == s[i]:
                if right -left > maxlength :
                    maxlength = right -left
                    start = left 
                    end = right
                left -= 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right+1 -left > maxlength :
                    maxlength = right -left+1
                    start = left
                    end = right +1
                left -= 1
                right += 1
        print(s[start:end])
        return s[start:end]