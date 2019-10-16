
class Solution:
    # my solution
    def bin_search(self,nums,start,end,target):

        if start > end:
            return -1
        l,r = start,end
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1

    def search(self, nums, target):

        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return -1 if nums[0] != target else 0
        if nums[-1] > nums[0]:
            return self.bin_search(nums,target)

        # find pivot:
        l,r = 0,len(nums)-1
        pivot = 0
        while l <= r:
            if r - l == 1:
                if nums[r] > nums[l]:
                    pivot = l
                else:
                    pivot = r
                break
            mid = (l+r) // 2
            if nums[mid] > nums[l] and nums[mid] > nums[r]:
                l = mid
            elif nums[mid] < nums[l] and nums[mid] < nums[l]:
                r = mid

        rs1 = self.bin_search(nums,0,pivot-1,target)
        rs2 = self.bin_search(nums,pivot,len(nums)-1,target)
        if rs1 == -1 and rs2 == -1:
            return -1
        elif rs1 != -1:
            return rs1
        else:
            return rs2

class Solution_:
    # better one
    def search(self, nums, target):

        pass

print(Solution().search([4,5,6,7,0,1,2],3))