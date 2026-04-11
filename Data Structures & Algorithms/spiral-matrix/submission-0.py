class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if not matrix:
            return result
        
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])
        
        while left < right and top < bottom:
            # Traverse from left to right along the top row
            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1
            
            # Traverse from top to bottom along the right column
            for i in range(top, bottom):
                result.append(matrix[i][right - 1])
            right -= 1
            
            # Check if we still have rows/columns to traverse
            if not (left < right and top < bottom):
                break
            
            # Traverse from right to left along the bottom row
            for i in range(right - 1, left - 1, -1):
                result.append(matrix[bottom - 1][i])
            bottom -= 1
            
            # Traverse from bottom to top along the left column
            for i in range(bottom - 1, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
        return result