class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        copy = list(nums)
        for i in range(0 , len(nums)):
            nums[(i+k)%len(nums)] = copy[i]
        print(copy)
