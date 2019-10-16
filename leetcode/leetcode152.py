"""
152. Maximum Product Subarray
tag:DP
"""
"""
example:[2,3,-2,4]
        [2,1,3,-10,-1,-2]
"""
class Solution:

    def maxProduct(self, nums):

        if len(nums) == 0:
            return None

        cur_max = None
        cur_min = None
        global_max = -float('inf')

        for num in nums:

            if cur_max is None and cur_min is None:
                cur_max = num
                cur_min = num

            tmp = cur_max * num
            cur_max = max(num,tmp,num*cur_min)
            cur_min = min(num,tmp,num*cur_min)
            global_max = max(cur_max,global_max)

        return global_max