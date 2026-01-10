class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        """
            1. Traverse through both strings character by character using Dynamic Programming.
            2. Find the CS with the maximum ASCII sum.
            3. Keep this subsequence in both strings.
            4. Delete all other characters from both strings.
            5. Calculate:
                min_sum = asciiSum(s1) + asciiSum(s2) − 2 × asciiSum(MCS)
            6. Return min_sum.
        """
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1): # i → s1
            for j in range(1, n + 1): # j → s2
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + ord(s1[i - 1])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        ascii_sum1 = sum(ord(c) for c in s1)
        ascii_sum2 = sum(ord(c) for c in s2)

        return ascii_sum1 + ascii_sum2 - 2 * dp[m][n]


"""
Time Complexity: O(m × n) - DP over both strings

Space Complexity: O(m × n) – DP table storage
"""