class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        mat = grid.copy()
        for i in range(len(grid)-1,-1,-1):
            for j in range(len(grid[0])-1,-1,-1):
                if i == len(grid) -1 and j == len(grid[0])-1:
                    pass
                elif  i == len(grid) -1:
                    mat[i][j] += mat[i][j+1]
                elif  j == len(grid[0]) -1:
                    mat[i][j] += mat[i+1][j]
                else:
                    mat[i][j] += min(mat[i+1][j],mat[i][j+1])
                    
        return mat[0][0]
        
                    
                    
                
