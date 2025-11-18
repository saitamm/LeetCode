class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        for i in range(0, len(grid[0])):
            low = 0
            high = len(grid) -1
            while low <= high:
                mid = low + (high - low)/2
                if grid[high][i] > 0:
                    break
                if grid[mid][i] >= 0 :
                    low = mid + 1
                if (grid[mid][i] < 0):
                    count += high -mid+1
                    high = mid -1
        return count
                
                