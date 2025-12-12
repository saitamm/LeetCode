class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums)-1
        while True:
            mid = low + (high -low)/2
            print(mid , low, high)
            if mid == 0 or mid ==  len(nums)-1 :
                return nums[mid]
            if mid % 2 == 0 :
                if nums[mid] == nums[mid+1]:
                    low= mid +1 
                elif nums[mid] == nums[mid-1]:
                    high = mid-1
            if mid % 2 != 0 :
                if nums[mid] == nums[mid-1]:
                    low= mid+1
                elif nums[mid] == nums[mid+1]:
                    high = mid-1
            if nums[mid] != nums[mid+1] and nums[mid] != nums[mid-1]:
                return(nums[mid])
        return (-1)

        