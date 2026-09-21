class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        op=[0]*k
        dp=[0]*k
        for num in nums:
            new=[0]*k
            new[num%k]+=1
            for r in range(k):
                new[(r*num)%k]+=dp[r]
            dp=new
            for r in range(k):
                op[r]+=dp[r]
        return op

