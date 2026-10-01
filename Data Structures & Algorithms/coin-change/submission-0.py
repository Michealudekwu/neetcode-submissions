class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        # dp[i][j] = minimum number of coins needed
        # to make amount j using the first i coins
        dp = [[float("inf")] * (amount + 1) for _ in range(n + 1)]

        # 0 coins are needed to make amount 0
        for i in range(n + 1):
            dp[i][0] = 0

        # Fill the table
        for i in range(1, n + 1):
            for j in range(1, amount + 1):

                # Don't use the current coin
                dp[i][j] = dp[i - 1][j]

                # Use the current coin if it fits
                if coins[i - 1] <= j:
                    dp[i][j] = min(
                        dp[i][j],
                        1 + dp[i][j - coins[i - 1]]
                    )

        # If amount is impossible, return -1
        if dp[n][amount] == float("inf"):
            return -1

        return dp[n][amount]