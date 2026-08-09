class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        n,m=len(discounts),len(prices)
        x=min(m,n)
        print(prices)
        ans=0
        for i in range(x):
            ans+=(prices[i]*(100-discounts[i]))/100
        if m>n:
            for i in range(n,m):
                ans+=prices[i]
        return ans
            
            