class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        c=Counter(bulbs)
        op=[]
        for i in set(bulbs):
            if c[i]%2!=0:
                op.append(i)
        op.sort()
        return op