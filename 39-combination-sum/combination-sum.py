class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def comb(ind,target,stack):
            if target==0:
                res.append(stack.copy())
                return
            if ind==len(candidates) or candidates[ind]>target: return 
            stack.append(candidates[ind])
            comb(ind,target-candidates[ind],stack)
            stack.pop()
            comb(ind+1,target,stack)
        comb(0,target,[])
        return res


            
                



        