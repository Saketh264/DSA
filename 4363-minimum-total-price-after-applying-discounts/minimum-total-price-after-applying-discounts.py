class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        x=min(len(discounts),len(prices))
        tot=sum(prices)
        for i in range(x):
            tot-=(prices[i]*discounts[i]/100)
        return tot
            
            