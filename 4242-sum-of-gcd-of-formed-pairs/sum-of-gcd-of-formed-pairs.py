class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        maxi=float('-inf')
        op=[]
        for i in range(len(nums)):
            maxi=max(maxi,nums[i])
            gcd=math.gcd(maxi,nums[i])
            op.append(gcd)
        op.sort()
        m=len(op)
        sums=0
        final_gcd=float('-inf')
        for i in range(m//2):
            sums+=math.gcd(op[i],op[m-i-1])
        return sums