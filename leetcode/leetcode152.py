"""
152. Maximum Product Subarray
tag:DP
"""
"""
example:[2,3,-2,4]
"""
class Solution:

    def maxProduct(self, nums):

        if len(nums) == 0:
            return None
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1,len(nums)):
            pass

