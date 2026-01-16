class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        """
        Algorithm
            1. Sort the horizontal bars and vertical bars.
            2. For each bar list:
            - Find the maximum length of consecutive values.
            3. Take the minimum of the two maximum lengths as the square side.
            4. Return the square of the side length.
        """
        def maxLen(Bars: List[int]):
            count,length = 2,2
            for i in range(1,len(Bars)):
                if Bars[i] - Bars[i-1] == 1: count += 1
                else: count = 2
                length = max(length, count)
            return length
        hBars.sort(), vBars.sort()
        side = min(maxLen(hBars), maxLen(vBars))
        return side * side
"""
Complexity:
Time: O(n log n) - Sorting
Space : O(1) - Constant
"""