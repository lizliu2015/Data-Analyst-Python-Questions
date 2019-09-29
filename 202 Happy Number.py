def isHappy(self, n):
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum([int(x) **2 for x in str(n)])
        return n == 1

class Solution:
    def isHappy(self, n):
        s = set()
        while n != 1:
            sum = 0
            for i in str(n):
                sum = int(i)**2 + sum 
            n = sum 
            if n in s:
                return False
            else:
                s.add(n) 
        return True
