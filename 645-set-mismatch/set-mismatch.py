class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mylist = list(range(1, len(nums) + 1))
        remove = 0
        for i in range(0, len(nums)):
            if nums[i] in mylist:
                mylist.remove(nums[i])
            else:
                remove = nums[i]
        mylist.insert(0, remove )
        return mylist