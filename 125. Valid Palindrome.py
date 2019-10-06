class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = []
        for i in s:
            if i.isalnum():
                l.append(i.lower())
        
        for j in range(len(l)//2):
            if l[j] != l[len(l)-j-1]:
                return False
        return True
