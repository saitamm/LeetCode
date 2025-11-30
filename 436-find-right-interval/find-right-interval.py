class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        n = len(intervals)
        pairs = [None] * n
        result = []
        for i in range(0,len(intervals)):
            pairs[i] = [intervals[i][0], i]
        pairs.sort()
        for i in range(0, len(intervals)):
            num = intervals[i][1]
            low = 0
            high = len(intervals)-1
            index = -1
            while low <= high:
                mid = (low + high)/2
                if pairs[mid][0] < num:
                    low = mid + 1
                elif pairs[mid][0] >= num :
                    index = pairs[mid][1]
                    high = mid -1
            result.append(index)
        return result