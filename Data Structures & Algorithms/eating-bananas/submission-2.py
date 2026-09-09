class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        hi = 0
        lo = 0
        for pile in piles:
            hi = max(pile, hi)
        mid = (hi+lo)//2
        bestRate = hi
        while lo <= hi:
            if self.canFinish(mid, piles, h):
                hi = mid-1
                bestRate = min(bestRate, mid)
            else:
                lo = mid+1
            mid = (hi+lo)//2
        return bestRate 
    def canFinish(self, rate: int, piles: list[int], h: int) -> bool:
        sumHours = 0
        if rate == 0:
            return False
        for pile in piles:
            pile_time = -(pile//-rate)
            sumHours += pile_time
        if sumHours > h:
            return False
        else:
            return True