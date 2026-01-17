class Solution:
    def largestSquareArea(self, bl: List[List[int]], tr: List[List[int]]) -> int:
        """
        Algorithm:
            1. For each rectangle pair(s), find overlapping area of them.
            2. Then, take the smaller of width or height as the square side.
            3. Keep the maximum side found.
            4. Return side².
        """
        side = 0 # maximum side
        n = len(bl)

        # Traverse through the rectangle pairs
        for i in range(n):
            for j in range(i + 1, n):
                min_x = max(bl[i][0], bl[j][0])
                max_x = min(tr[i][0], tr[j][0])
                min_y = max(bl[i][1], bl[j][1])
                max_y = min(tr[i][1], tr[j][1])

                # Largest Area
                if min_x < max_x and min_y < max_y:
                    length = min(max_x - min_x, max_y - min_y)
                    side = max(side, length)

        return side * side 
"""
Complexity:
Time : O(n^2)
Space : O(1)
"""