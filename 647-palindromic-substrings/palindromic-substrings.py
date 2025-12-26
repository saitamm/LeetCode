class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(0, len(s)):
            left = i
            right = i + 1
            while left >= 0 and s[left] == s[i]:
                res += 1
                left -= 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        return res