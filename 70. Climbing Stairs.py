# O(2^N)
class Solution:
    def climbStairs(self, n: int) -> int:        
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)


# O(N) dynamic programming
class Solution:
    memo = {}
    def climbStairs(self, n: int) -> int:        
        if n == 1: 
            return 1
        if n == 2: 
            return 2
        
        if n in self.memo:
            return self.memo[n]
        
        output = self.climbStairs(n-1) + self.climbStairs(n-2)
        
        if n not in self.memo:
            self.memo[n] = output
        
        return output
