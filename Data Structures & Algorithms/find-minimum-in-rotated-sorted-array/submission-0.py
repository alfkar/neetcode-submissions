class Solution:
    def findMin(self, nums: list[int]) -> int:
        lo = 0
        hi = len(nums)-1
        mid = (lo+hi)//2
        while lo < hi:
            if nums[mid] <= nums[hi]:
                hi = mid
            else:
                lo = mid+1
            mid = (lo+hi)//2
        return nums[hi]