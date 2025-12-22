class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        low = 0
        high = len(arr) -1
        idx = 0
        while high >= low :
            mid = (low + high)/2
            if arr[mid] <= arr[mid+1]:
                low = mid + 1
            else :
                high = mid -1
                idx = mid
        return (idx)
        