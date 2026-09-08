class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        l = 0
        h = len(matrix)-1
        m = (l+h)//2
        while l<=h:
            if matrix[m][0] > target:
                h = m-1
            elif matrix[m][0] < target:
                l = m+1
            else:
                break;
            m = (l+h)//2
        return self.searchRow(matrix[m], target)
    def searchRow(self, row: list[int], target: int) -> bool:
        l = 0
        h = len(row)-1
        m = (l+h)//2
        while l<=h:
            if row[m] > target:
                h = m-1
            elif row[m] < target:
                l = m+1
            elif row[m] == target:
               return True 
            m = (l+h)//2
        return False