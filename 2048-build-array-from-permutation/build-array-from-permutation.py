class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # Just do it : Hint 1 => Just apply what's said in the statement.
        ans = []
        for idx,val in enumerate(nums):
            perm_arr = nums[nums[idx]]
            ans.append(perm_arr)
        return ans # wtf i solved it in 10 sec 