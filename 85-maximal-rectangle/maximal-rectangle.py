class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0 # Base Case

        rows, cols = len(matrix), len(matrix[0])
        height = [0] * (cols + 1) # flushing
        max_area = 0

        for row in matrix:
            for i in range(cols):
                # Update height based on current row(hist base)
                if row[i] == '1':
                    height[i] += 1
                else:
                    height[i] = 0
                
            # Largest Rectangle in Hist
            stack = [-1] # pointer
            for i in range(cols + 1):
                while stack[-1] != -1 and height[stack[-1]] >= height[i]:
                    l = height[stack.pop()] # length
                    b = i - stack[-1] - 1 # breadth
                    max_area = max(max_area, l * b) # maximum area of rect -> max(l x b)
                stack.append(i)
        return max_area

"""
Complexity:
Time: O(NxM) -> Traversal x pushed/popped from the stack 
Space: O(M) -> No of Columns
"""