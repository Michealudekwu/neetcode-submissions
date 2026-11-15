class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        n = len(prices)

        l,r = 0, 1

        while l < n-1:
            while prices[r] > prices[l]:
                max_prof = max(max_prof, (prices[r] - prices[l]))
                r += 1
                if r > n-1:
                    break

            l = r
            r += 1
        
        return max_prof
        