class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # Transpose the matrix
        for row in range(n):
            for col in range(row + 1, n):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        # Reverse the row   
        for row in matrix:
            row.reverse()

        return (matrix)
"""
Complexity:
Time Complexity: O(n^2) - Every element is visited -> swapped 'n' times
Space Complexity: O(1) - Modifying within the matrix
"""