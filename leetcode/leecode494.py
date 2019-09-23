"""
494. Target Sum
tag: DP
"""
"""
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.
"""

class Solution:

    result_count = 0

    def search(self, nums, cur_idx, cur_sum, target_sum):

        if cur_idx >= len(nums):
            return



        if cur_sum == target_sum:
            self.result_count += 1



    def findTargetSumWays(self, nums, S):
        pass

