class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        current_max = (r-l)*min(heights[l],heights[r])
        while r>l:
            h = min(heights[l],heights[r])
            w = r-l
            v = h*w
            current_max = max (v, current_max)
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
        return current_max
                