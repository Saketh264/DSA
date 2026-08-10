class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans=[]
        def comb(ind,target,stack):
            if target==0: 
                ans.append(stack.copy())
                return
            for i in range(ind,len(candidates)):
                if i>ind and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>target:
                    break
                stack.append(candidates[i])
                comb(i+1,target-candidates[i],stack)
                stack.pop()
        comb(0,target,[])
        return ans