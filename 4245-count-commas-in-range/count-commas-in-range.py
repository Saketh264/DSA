class Solution:
    def countCommas(self, n: int) -> int:
        x=len(str(n))
        if x<4: return 0
        else: return (int(n)-1000+1)
        # 1,000--4
        # 10,000--5
        # 1,00,000--6
        # 10,00,000--7
        # 1,00,00,000--8