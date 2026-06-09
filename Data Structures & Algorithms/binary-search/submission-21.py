class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        half = math.ceil((len(nums) - 1) / 2)

        while left <= right:
            if nums[half] == target:
                return half
            if nums[half] < target:
                left = half + 1
                half = math.ceil((left + right) / 2)
            else:
                right = half - 1
                half = math.floor((left + right) / 2)
        return -1