class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        for i in range(len(str(x))//2):
            if str(x)[i] != str(x)[len(str(x))-i-1]:
                return False
        return True
