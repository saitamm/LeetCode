class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}
        index = 0
        for i in range(0, len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            while (index <= i and count[s[index]] >= 2):
                index += 1
        if (index >= len(s)):
            return (-1)
        return(index)