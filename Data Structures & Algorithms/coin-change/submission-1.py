class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [float("inf")] * (amount+1)
        dp[0] = 0
        print(dp)

        for i in range(n):
            for j in range(1, len(dp)):
                # if coins[i] >= dp[j]
                if coins[i] <= j:
                    dp[j] = min(dp[j], 1 + dp[j - coins[i]]) #for next column 
       
        print(dp)

        return dp[amount] if dp[amount] != float("inf") else -1