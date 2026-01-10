class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        miss_num = sum(range(len(nums)+1)) - sum(nums) # sum(N(N+1)) - sum(N)
        return miss_num
        