class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def makeItZero(list_,row,column):
            for i in range(len(list_[0])):
                list_[row][i] = 0
            for i in range(len(list_)):
                list_[i][column] = 0
                
        zeros_rows = []
        zeros_columns = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] ==0:
                    zeros_rows.append(row)
                    zeros_columns.append(col)
        for i in range(len(zeros_rows)):
            makeItZero(matrix,zeros_rows[i],zeros_columns[i])
                
                    
        