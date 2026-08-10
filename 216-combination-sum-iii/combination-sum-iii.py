class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        candidate=[1,2,3,4,5,6,7,8,9]
        def comb(i,n,stack):
            if len(stack)==k :
                if n==0:
                    ans.append(stack.copy())
                return
            if i==len(candidate): return
            stack.append(candidate[i])
            comb(i+1,n-candidate[i],stack)
            stack.pop()
            comb(i+1,n,stack)
        comb(0,n,[])
        return ans