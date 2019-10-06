class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        for i in range(1,x//2+1):
            if i**2 <= x and (i+1)**2 > x:
                return i
                
#binary search                
class Solution:
    def mySqrt(self, x: int) -> int:
            def mySqrt(self, x):
        lo, hi = 0, x
        
        while lo <= hi:
            mid = (lo + hi) // 2
            
            if mid * mid > x:
                hi = mid - 1
            elif mid * mid < x:
                lo = mid + 1
            else:
                return mid
        
        # When there is no perfect square, hi is the the value on the left
        # of where it would have been (rounding down). If we were rounding up, 
        # we would return lo
        return hi
