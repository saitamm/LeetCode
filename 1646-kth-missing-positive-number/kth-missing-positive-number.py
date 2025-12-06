class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        start = 1 
        length = 1
        missing = []
        while len(missing) <= k:
            if start in arr :
                start +=1
                continue
            else:
                missing.append(start)
            start+=1
        return missing[k-1]
        