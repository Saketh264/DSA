class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        maxi=float('-inf')
        op=[]
        for i in range(len(nums)):
            maxi=max(maxi,nums[i])
            op.append(math.gcd(maxi,nums[i]))
        op.sort()
        m=len(op)
        sums=0
        for i in range(m//2):
            sums+=math.gcd(op[i],op[m-i-1])
        return sums