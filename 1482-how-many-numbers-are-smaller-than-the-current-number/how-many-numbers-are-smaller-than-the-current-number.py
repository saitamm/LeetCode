class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = [0] * len(nums)
        for i in range(0, len(nums)):
            for j in range(0, i):
                if (nums[i] < nums[j]):
                    count[j]+=1
                elif (nums[i] > nums[j]):
                    count[i]+=1
        print(count)
        return (count)
