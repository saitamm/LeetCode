class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # (0,0) → (0,2) → (2,2) → (2,0) → back to (0,0)
        n= len(matrix[0])
        for i in range(0, n//2):
            for j in range(i, n-1-i):
                top = [i, j]
                right = [j , n-1-i]
                buttom = [n-1-i, n-1-j]
                left = [n-1-j, i]
                temp = matrix[top[0]][top[1]]
                matrix[top[0]][top[1]] = matrix[left[0]][left[1]]
                matrix[left[0]][left[1]] = matrix[buttom[0]][buttom[1]]
                matrix[buttom[0]][buttom[1]] = matrix[right[0]][right[1]]
                matrix[right[0]][right[1]] = temp 
