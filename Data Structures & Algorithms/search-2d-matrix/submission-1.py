class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        up = 0 
        bottom = n - 1

        while up <= bottom:
            mid_row = up + (bottom - up) // 2
                
            if target > matrix[mid_row][-1]:
                up = mid_row + 1
            elif target < matrix[mid_row][0]:
                bottom = mid_row - 1
            elif target >= matrix[mid_row][0] and target <= matrix[mid_row][-1]:
                l, r = 0, m - 1  
                while l <= r:
                    mid_col = l + (r - l) // 2
                    if target == matrix[mid_row][mid_col]:
                        return True
                    elif target > matrix[mid_row][mid_col]:
                        l = mid_col + 1
                    else:
                        r = mid_col - 1 
                break        

        return False    

