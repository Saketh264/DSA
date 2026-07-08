class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD=10**9+7
        n=len(s)
        digits=[]
        pos=[]
        for i, ch in enumerate(s):
            if ch!='0':
                digits.append(int(ch))
                pos.append(i)
        k=len(digits)
        prefSum=[0]*(k+1)
        prefVal=[0]*(k + 1)
        pow10=[1]*(k + 1)
        for i in range(1, k + 1):
            pow10[i]=pow10[i-1]*10%MOD
            prefSum[i]=prefSum[i-1]+digits[i -1]
            prefVal[i]=(prefVal[i-1]*10 +digits[i - 1]) % MOD
        nxt = [k] * (n + 1)
        p = k - 1
        for i in range(n - 1, -1, -1):
            while p >= 0 and pos[p] > i:
                p -= 1
            if p >= 0 and pos[p] == i:
                nxt[i] = p
            elif p + 1 < k:
                nxt[i] = p + 1
            else:
                nxt[i] = k
        prv = [-1] * n
        p = 0
        last = -1
        for i in range(n):
            if p < k and pos[p] == i:
                last = p
                p += 1
            prv[i] = last

        ans = []
        for l, r in queries:
            L = nxt[l]
            R = prv[r]
            if L > R or L == k or R == -1:
                ans.append(0)
                continue
            length = R - L + 1
            x = (prefVal[R + 1] -
                 prefVal[L] * pow10[length]) % MOD
            sm = prefSum[R + 1] - prefSum[L]
            ans.append((x * sm) % MOD)
        return ans