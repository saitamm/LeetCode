class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        left = 0
        arr_sort = sorted(arr)
        expect = -1
        while left < len(arr)-1 :
            if expect == -1:
                expect = arr_sort[left+1] - arr_sort[left]
            if  arr_sort[left+1] - arr_sort[left]  != expect:
                return (False)
            left+=1
        return (True)
        