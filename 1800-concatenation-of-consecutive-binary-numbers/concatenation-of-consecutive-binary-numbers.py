class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans=0
        MOD=10**9+7
        for i in range(1,n+1):
            bits=i.bit_length()
            ans=((ans<<bits)|i)%MOD
        return ans