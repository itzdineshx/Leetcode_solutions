class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sort_arr = (num*num for num in nums)
        ans = sorted(sort_arr)
        return ans