class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        line = len(matrix)
        col = len(matrix[0])
        up = 0
        down = line -1
        left = 0
        right = col - 1
        m = 0
        while m < col*line:
            if up <= down:
                for i in range(left, right+1):
                    result.append(matrix[up][i])
                    m+=1
            up += 1
            if left <= right:
                for i in range(up, down+1):
                    result.append(matrix[i][right])
                    m+=1
            right-=1
            if down  >= up:
                for i in range(right, left-1, -1):
                    result.append(matrix[down][i])
                    m+=1
            down -= 1
            if right >= left:
                for i in range(down, up-1, -1):
                    result.append(matrix[i][left])
                    m+=1
            left+=1
        return(result)