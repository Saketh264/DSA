class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dick=defaultdict(int)
        res=0
        i=0
        for j in range(len(s)):
            dick[s[j]]+=1
            maxfreq=max(dick.values())
            curr=j-i+1
            if curr-maxfreq>k:
                dick[s[i]]-=1
                i+=1
            res=max(res,j-i+1)
        return res