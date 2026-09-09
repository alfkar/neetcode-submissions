class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        hi = max(piles) 
        lo = 1
        mid = (hi+lo)//2
        while lo < hi:
            if self.canFinish(mid, piles, h):
                hi = mid
            else:
                lo = mid+1
            mid = (hi+lo)//2
        return hi 
    def canFinish(self, rate: int, piles: list[int], h: int) -> bool:
        sumHours = 0
        for pile in piles:
            pile_time = -(pile//-rate)
            sumHours += pile_time
            if(sumHours > h):
                return False
        return True

