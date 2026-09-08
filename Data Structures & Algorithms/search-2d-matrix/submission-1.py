class Solution:
    def bsearch(self, n: int, target: int, get) -> int:
        lo, hi = 0, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if get(mid) > target:   hi = mid - 1
            elif get(mid) < target: lo = mid + 1
            else: return mid
        return hi

    def searchMatrix(self, matrix, target) -> bool:
        r = self.bsearch(len(matrix), target, lambda i: matrix[i][0])
        if r < 0: return False
        row = matrix[r]
        c = self.bsearch(len(row), target, lambda i: row[i])
        return c >= 0 and row[c] == target
