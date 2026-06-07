from sys import maxsize
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        window = {}
        windowMax = -maxsize
        left = 0
        for i in range(0, k):
            window[nums[i]] = window.get(nums[i], 0) + 1
            windowMax = max(windowMax, nums[i])
        result = [windowMax]
        for right in range(k, len(nums)):
            if k < 2:
                windowMax = -maxsize
            window[nums[right]] = window.get(nums[right], 0) + 1
            leftElem = nums[left]
            window[leftElem] = window.get(leftElem, 0) - 1
            if window[leftElem] == 0:
                del window[leftElem]
            if nums[left] >= windowMax:
                windowMax = -maxsize
                for key, val in window.items():
                    windowMax = max(key, windowMax)
            if nums[right] > windowMax:
                windowMax = nums[right]
            result = result + [windowMax]
            left += 1
        return result