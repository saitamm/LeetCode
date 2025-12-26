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
                print("----")
                res += 1
                left -= 1
            while left >= 0 and right < len(s) :
                if s[left] == s[right]:
                    print("^^^^^^")
                    res += 1
                else :
                    break
                left -= 1
                right += 1
            print("i am heere")

        return res