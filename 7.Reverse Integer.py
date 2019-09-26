#mathmatical
class Solution(object):
    def reverse(self, x):
        result = 0
        symbol = 1
        
        if x < 0:
            symbol = -1
            x = -x

        while x:
            result = result * 10 + x % 10
            x /= 10
            
        return 0 if result > pow(2,31) else result * symbol
 
# reverse index
def reverse(x):
  res = str(abs(x))
  res = int(res[::-1])
  
  if x > 0:
    return res
  else:
    return -res

