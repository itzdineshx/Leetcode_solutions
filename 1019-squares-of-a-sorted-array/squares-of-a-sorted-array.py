class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Approach 1 - Using sorting
        # sort_arr = [num*num for num in nums]
        # sort_arr.sort()
        # return sort_arr
        """
        Complexity:
        Time - O(n log n)
        Space - O(n)
        """

        # Approach 2 - Using Two pointer
        l , r = 0 , len(nums)-1
        sort_arr = []
        while l<=r:
            if abs(nums[l]) < abs(nums[r]):
                sort_arr.append(nums[r]**2)
                r -= 1
            else:
                sort_arr.append(nums[l]**2)
                l += 1
        return sort_arr[::-1]
        
        """
        Complexity:
        Time - O(n)
        Space - O(n)
        """