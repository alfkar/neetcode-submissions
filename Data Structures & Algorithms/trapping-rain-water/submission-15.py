class Solution:
    def trap(self, height: list[int]) -> int:
        volume = 0
        l=0
        r=1
        l_max = (height[0],0)
        r_max = (0,0)
        bumps = 0
        while (r<=len(height)-1):
            if height[r] >= l_max[0]:
                if(l_max[0] != 0):
                    volume += ((r-l-1)*l_max[0])-bumps
                l_max = (height[r],r)
                r_max = (max(height[r], r_max[0]),r_max[1])
                bumps=0
                l=r
                r+=1
            else: 
                bumps += height[r]
                if r != len(height):
                    r_max = (max(height[r], r_max[0]),r_max[1])
                r += 1
        bumps = 0
        r=len(height)-1
        r_max = (height[r], r)
        l=r-1
        while (l >= l_max[1]):
            if height[l] >= r_max[0]:
                if(r_max[0] != 0):
                     volume += ((r-l-1)*r_max[0])-bumps
                r_max = (height[l],l)
                r=l
                l-=1
                bumps=0
            else: 
                bumps += height[l]
                l -= 1
        return volume
