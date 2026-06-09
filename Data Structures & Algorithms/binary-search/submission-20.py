class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        half = math.ceil((len(nums)-1)/2)
        while left < right:
            if nums[half] == target:
                return half
            if nums[half] < target:
                left = half
                half = math.ceil((left+right)/2)
                left += 1
            else:
                right = half
                half = math.floor((left+right)/2)
                right -=1
        if nums[half] == target:
            return half
        return -1
