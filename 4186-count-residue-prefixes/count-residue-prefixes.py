class Solution:
    def residuePrefixes(self, s: str) -> int:
        residue_cnt = 0
        for i in range(len(s)):
            prefix = s[:i+1]
            if len(set(prefix)) == len(prefix) % 3:
                residue_cnt += 1
        return residue_cnt