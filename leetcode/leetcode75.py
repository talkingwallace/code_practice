"""
75. Sort Colors
"""


class Solution:

    def bi_part(self,arr,start,end,pivot_val=0):

        if start > end:
            return -1
        while end > start:
            while arr[end] != pivot_val and end > start:
                 end -= 1
            while arr[start] <= pivot_val and end > start:
                 start += 1
            if start >= end:
                break
            tmp = arr[end]
            arr[end] = arr[start]
            arr[start] = tmp
        return end


    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s = set(nums)
        if 0 in s:
            mid = self.bi_part(nums,0,len(nums)-1,pivot_val=0)
        else:
            mid = -1
        if 1 in s:
            self.bi_part(nums,mid+1,len(nums)-1,pivot_val=1)


if __name__ == '__main__':
    arr = [2,1]
    print(Solution().sortColors(arr))