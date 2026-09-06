class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0]*(n+2)
        for i in range(n-1,-1,-1):
            pick=nums[i]
            pick+=dp[i+2]
            not_pick=dp[i+1]
            maxi=max(pick,not_pick)
            dp[i]=maxi
        return dp[0]
        # def dp(ind):
        #     if ind>=len(nums): return 0
        #     pick=nums[ind]+dp(ind+2)
        #     notpick=dp(ind+1)
        #     maxi=max(pick,notpick)
        #     return maxi
        # return dp(0)