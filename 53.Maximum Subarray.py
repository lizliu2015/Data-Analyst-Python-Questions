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
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = nums.copy()
        for i in range(1, len(nums)):
            if dp[i-1] > 0:
                dp[i] = dp[i-1] + nums[i]
        return max(dp)
#If the sum of a subarray is positive, it has possible to make the next value bigger, so we keep do it until it turn to negative.
#If the sum is negative, it has no use to the next element, so we break.
#it is a game of sum, not the elements.
