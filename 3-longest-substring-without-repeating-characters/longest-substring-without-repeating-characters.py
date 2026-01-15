class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen = set()
        max_len = 0
        left = 0

        for i in range(n):
            while s[i] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[i])
            max_len = max(max_len, i - left + 1)
        return(max_len) 