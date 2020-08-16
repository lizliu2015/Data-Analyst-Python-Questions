class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        p1 = 0 
        d = {}
        lmax = 1
        for p2 in range(len(s)):
            if s[p2] in d.keys() and p1 <= d[s[p2]] < p2: #repeating characters, move p1 next to the repeating characters
                p1 = d[s[p2]] + 1
                d[s[p2]] = p2
            else:
                d[s[p2]] = p2
                lmax = max(lmax, p2-p1+1)
        return lmax
