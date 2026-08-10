class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def comb(ind,target,stack):
            if ind==len(candidates):
                if target==0:
                    res.append(stack.copy())
                return
            if candidates[ind]<=target:
                stack.append(candidates[ind])
                comb(ind,target-candidates[ind],stack)
                stack.pop()
            comb(ind+1,target,stack)
        comb(0,target,[])
        return res


            
                



        