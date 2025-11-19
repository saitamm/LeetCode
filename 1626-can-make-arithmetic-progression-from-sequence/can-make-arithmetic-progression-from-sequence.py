class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        expect = arr[1]-arr[0]
        left = 1
        while left < len(arr)-1 :
            current = arr[left+1] - arr[left]
            if  (current) != expect:
                return (False)
            left+=1
        return (True)
        