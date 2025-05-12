class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0,len(matrix)-1
        while l <= r:
            mid = (l+r)//2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                r = mid-1
            else:
                l = mid+1
        
        row = matrix[min(l,r)]
        l,r = 0,len(row)-1
        while l <= r:
            mid = (l+r)//2
            if row[mid] == target:
                return True
            elif row[mid] > target:
                r = mid-1
            else:
                l = mid+1

        return False