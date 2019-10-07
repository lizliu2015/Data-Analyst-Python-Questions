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
        if x == 0:
            return 0
        if x == 1:
            return 1
        l = 0
        h = x
        while l <= h:
            mid = (l+h)//2         
            if mid**2 <= x < (mid+1)**2:
                return mid
            elif mid**2 < x:
                l = mid+1 
            elif mid**2 > x:
                h = mid-1


class Solution:
    def mySqrt(self, x: int) -> int:
        return self.bsearch(0, x, x)
                
    def bsearch(self, low: int, high: int, target: int) -> int:
        mid = (high + low)//2
        if mid**2 <= target and (mid+1)**2 > target: # this was the tricky part for me
            return mid
        elif mid**2 > target:
            return self.bsearch(low, mid-1, target)
        else:
            return self.bsearch(mid+1, high, target)
