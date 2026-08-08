class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        ans=[]
        for top in words:
            for left in words:
                if top==left or top[0]!=left[0]:
                    continue
                for right in words:
                    if right==top or right==left or right[0]!=top[3]:
                        continue
                    for bottom in words:
                        if bottom in (top,left,right):
                            continue
                        if bottom[0]==left[3] and bottom[3]==right[3]:
                            ans.append([top,left,right,bottom])
        return sorted(ans)