"""
416. Partition Equal Subset Sum
tag: recursive with memory

thinking:暴力 超时
thinking:排序+双指针 # 这个没用
thinking:搜索+记忆
"""
# 回溯法
# TLE
# class Solution:
#
#     flag = False
#
#     def search(self,nums,cur_sum,cur_idx,target_sum):
#
#         if cur_idx >= len(nums):
#             return
#         if self.flag == True:
#             return
#
#         if cur_sum + nums[cur_idx] < target_sum:
#
#             self.search(nums,cur_sum+nums[cur_idx],cur_idx+1,target_sum)
#             self.search(nums,cur_sum,cur_idx+1,target_sum)
#
#         elif cur_sum + nums[cur_idx] == target_sum:
#             self.flag = True
#             return
#         else:
#             self.search(nums,cur_sum,cur_idx+1,target_sum)
#
#     def canPartition(self, nums):
#
#         if len(nums) == 0:
#             return False
#
#         self.flag = False
#         sum = 0
#         for i in nums:
#             sum += i
#
#         # odd or even:
#         if sum & 1 == 1:
#             return False
#         target_sum = int(sum/2)
#
#         self.search(nums,0,0,target_sum)
#         return self.flag

class Solution:

    record = {}

    def search(self,nums,start_idx,target):

        if target < 0 or start_idx == len(nums):
            return False
        if target == 0:
            return True

        if (start_idx,target) in self.record:
            return self.record[(start_idx,target)]

        rs = self.search(nums,start_idx+1,target-nums[start_idx]) or self.search(nums,start_idx+1,target)
        self.record[(start_idx,target)] = rs
        return rs


    def canPartition(self, nums):

        self.record = {}
        if len(nums) == 0:
            return

        Sum = 0
        for i in nums:
            Sum += i

        if Sum & 1 == 1:
            return False

        rs = self.search(nums,0,Sum//2)
        print(self.record)
        return rs



if __name__ == '__main__':
    s = Solution()
    print(s.canPartition([1,1,3,5,2,3,4,1,2]))