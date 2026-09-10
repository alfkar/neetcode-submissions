class Solution:
    def search(self, nums: list[int], target: int) -> int:
        hi = len(nums)-1
        lo = 0
        while lo < hi:
            mid = (hi+lo)//2
            if nums[mid] < nums[hi]:
                hi = mid
            else:
                lo = mid + 1
        if nums[hi] <= target and target <= nums[len(nums)-1]:
            lo = hi
            hi = len(nums)-1
        else: 
            lo = 0
        while lo < hi:
            mid = (hi+lo)//2
            if nums[mid] >= target:
                hi = mid
            else:
                lo = mid + 1
        if nums[hi] == target:
            return hi
        else: 
            return -1

