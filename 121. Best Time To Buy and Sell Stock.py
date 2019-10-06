class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        m = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] - prices[i] > m:
                    m = prices[j] - prices[i]
        return m
  
#dynamic programming
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = []
        for i in range(1, len(prices)):
            diff.append(prices[i] - prices[i-1])
        
        curr_sum = 0
        curr_max = float('-inf')
        
        for j in diff:
            if curr_sum > 0:
                curr_sum = curr_sum + j
            else:
                curr_sum = j
            if curr_max < curr_sum:
                curr_max = curr_sum
        
        if curr_max > 0:
            return curr_max
        return 0    
                
