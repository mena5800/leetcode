class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [100000] * (amount+1)
        coins.sort()
        dp[0] = 0
        for i in range(1,amount+1):
            for j in range(len(coins)):
                if i < coins[j]:
                    break
                dp[i] = min(dp[i],dp[i-coins[j]])
            dp[i] +=1
        if dp[-1]  == 100000 or dp[-1] == 100001:
            return -1
        else:
            return dp[-1]
                
                

                
                
        