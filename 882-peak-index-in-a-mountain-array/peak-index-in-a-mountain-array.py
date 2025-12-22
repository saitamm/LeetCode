class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        bol = []
        bol.append('T')
        for i in range(0,len(arr)-1):
            if arr[i] <= arr[i+1]:
                bol.append('T')
            else :
                bol.append('F')
                return(i)
        return (-1)
        