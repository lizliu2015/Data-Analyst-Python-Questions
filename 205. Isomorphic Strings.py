class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1 = dict()
        d2 = dict()
        for i in range(len(s)): 
            if d1.get(s[i]): 
                if d1[s[i]] != t[i]:  
                    return False
            elif d2.get(t[i]):
                    if d2[t[i]] != s[i]:
                        return False
            else:
                d1[s[i]] = t[i] 
                d2[t[i]] = s[i] 
        return True
