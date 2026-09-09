class Solution:
    def findMin(self, nums: list[int]) -> int:
        lo = 0
        hi = len(nums)-1
        while lo < hi:
            mid = (lo+hi)//2
            if nums[mid] <= nums[hi]:
                hi = mid
            else:
                lo = mid+1
        return nums[hi]