class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        result = [[intervals[0][0], intervals[0][1]]]
        j=0
        for i in range(1, len(intervals)):
            # print("===", intervals[i])
            # print("---", result[j][0])
            if (intervals[i][0] <= result[j][1]):
                # print("****")
                result[j][1] = max(intervals[i][1], result[j][1])
            else :
                result.append([intervals[i][0], intervals[i][1]])
                j+=1
        # print(result)
        return(result)
