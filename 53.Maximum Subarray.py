### O(N^2)
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = float("-inf")
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                s = sum(nums[i:j+1])
                if m < s:
                    m = s
        return m

###O(N)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        CurrMax = float('-inf')
        CurrSum = 0
        for i in range(len(nums)):
            if CurrSum > 0:
                CurrSum = nums[i] + CurrSum
            else:
                CurrSum = nums[i]
            if CurrSum > CurrMax:
                CurrMax = CurrSum
        return CurrMax
