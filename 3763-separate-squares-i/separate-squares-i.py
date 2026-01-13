class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = sum(l * l for _, _, l in squares) # Total area of all squares

        # Binary search bounds
        low = min(y for _, y, _ in squares) # lower bound
        high = max(y + l for _, y, l in squares) # upper bound

        def area_below(H):
            area = 0.0
            for _, y, l in squares:
                if H <= y:
                    continue
                elif H >= y + l:
                    area += l * l
                else:
                    area += l * (H - y)
            return area

        # Binary search for balance point
        eps = 1e-6
        while high - low > eps:
            mid = (low + high) / 2
            if area_below(mid) >= total_area / 2:
                high = mid
            else:
                low = mid

        return low

"""
Complexity:
Time: O(n log r)
space: O(1)
"""