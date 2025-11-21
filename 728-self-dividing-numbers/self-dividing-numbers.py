class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        L = []
        for i in range(left, right+1):
            nmbr = i
            flag = 0
            while nmbr != 0 :
                if (nmbr % 10) == 0 or i % (nmbr % 10) != 0  :
                    flag = 1
                    break
                nmbr = nmbr / 10
            if flag == 0:
                L.append(i)
        return L
        