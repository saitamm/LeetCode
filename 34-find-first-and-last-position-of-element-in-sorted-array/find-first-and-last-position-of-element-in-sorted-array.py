class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = [-1, -1]
        low = 0
        high = len(nums)-1
        pos = 0
        while low <= high :
            mid = low + (high -low)/2
            if (nums[mid] < target):
                low = mid+1
            if (nums[mid] >= target):
                high = mid-1
            if (nums[mid] == target) :
                pos = mid
        if pos < len(nums) and nums[pos] == target :
            index[0] = pos - (pos > 0 and nums[pos-1] == target)
            idx = 0
            while idx + pos < len(nums) and nums[idx+pos] == target :
                index[1] = pos + idx
                idx+=1
            return index
            print(index[0], "   " , index[1])
        
        return (index)
            
        