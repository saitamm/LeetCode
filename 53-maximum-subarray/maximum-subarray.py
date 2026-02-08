class Solution(object):
    def maxSubArray(self, nums):
        MaxSum = nums[0]
        Current = nums[0]
        for i in range(1, len(nums)):
            Current = max(nums[i], Current + nums[i])
            MaxSum = max(MaxSum, Current)
        return MaxSum