class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(x):
            if x<2: return False
            if x%2==0: return x==2
            i=3
            while i*i<=x:
                if x%i==0: return False
                i+=2
            return True

        if 8<=n<=11: return 11

        for i in range(1,100000):
            s=str(i)
            x=int(s+s[-2::-1])

            if x>=n and is_prime(x):
                return x