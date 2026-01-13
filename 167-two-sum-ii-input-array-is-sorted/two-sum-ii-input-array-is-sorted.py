class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Approach 1 - Brute force:
        # n = len(numbers)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if numbers[i]+numbers[j] == target:
        #             return(i+1, j+1)
        #             break
        """
        Complexity:
        Time: O(n^2) - Nested loop
        Space: O(1)
        """

        # Approach 2 - Two Pointer
        l, r = 0, len(numbers) -1
        while l < r:
            s = numbers[l] + numbers[r] 
            if s == target: # answer
                return l + 1, r + 1
            elif s < target: # move left pointer -> right
                l += 1
            else: # move right pointer -> left
                r -= 1
        return False
"""
Complexity:
Time: O(n) - Traversal
Space: O(1)
"""