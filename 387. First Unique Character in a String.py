class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = dict()
        for i in s:
            if counter.get(i):
                counter[i] = counter[i] + 1
            else: 
                counter[i] = 1
        
        for j in range(len(s)):
            if counter[s[j]] == 1:
                return j
        return -1
