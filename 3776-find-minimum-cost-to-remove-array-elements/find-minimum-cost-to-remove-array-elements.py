class Solution:
    def minCost(self, nums: List[int]) -> int:
        n=len(nums)
        @lru_cache(3_000)
        def dp(i,num):
            if i>=n:
                return num
            if i>=n-1:
                return max(nums[i],num)
            a,b,c=sorted([num,nums[i],nums[i+1]])
            cost1=c+dp(i+2,a)
            cost2=c+dp(i+2,b)
            cost3=b+dp(i+2,c)
            return min(cost1,cost2,cost3)
        return dp(1,nums[0])