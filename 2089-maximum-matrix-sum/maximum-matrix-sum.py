class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        neg_count = 0
        totalSum = 0
        min_abs = float('inf')
        for j in range(len(matrix)): # columns
            for i in range(len(matrix)): # rows
                if matrix[i][j] < 0: 
                    neg_count += 1
                abs_val = abs(matrix[i][j])
                totalSum += abs_val
                min_abs = min(min_abs, abs_val)
            
        return totalSum if neg_count % 2 == 0 else totalSum - 2 * min_abs