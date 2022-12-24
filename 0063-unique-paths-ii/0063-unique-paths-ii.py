class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = obstacleGrid.copy()
        if dp[-1][-1] == 1:
            return 0
        for i in range(len(obstacleGrid)-1,-1,-1):
            for j in range(len(obstacleGrid[0])-1,-1,-1):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                if i == len(obstacleGrid) -1 and j == len(obstacleGrid[0])-1:
                    dp[i][j] = 1
                elif i == len(obstacleGrid) -1:
                    if dp[i][j+1] == 0:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = 1
                elif j == len(obstacleGrid[0])-1:
                    if dp[i+1][j] == 0:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = 1
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]
        return dp[0][0]


            
        