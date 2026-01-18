class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        for target in nums1:
            next_g = -1
            found = False
        
            for num in nums2:
                if num == target:
                    found = True
                elif found:
                    if num > target:
                        next_g = num
                        break

            ans.append(next_g)
        return ans

"""
Complexity:
Time: O(m * n)
Space: O(1)
"""