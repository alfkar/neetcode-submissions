class Solution:
    def maxArea(self, heights: List[int]) -> int:
        height = min(heights[0],heights[1])
        current_max = height
        l=0
        r=1
        while l < len(heights)-2:
            height = min(heights[l],heights[r])
            width = r-l
            volume = height*width
            current_max = max(current_max, volume)
            if r < len(heights)-1:
                r+=1
            else:
                l+=1
                r=l+1
        return current_max
                