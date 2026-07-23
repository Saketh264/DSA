class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start,end=map(set,zip(*paths))
        destination=(end-start).pop()
        return destination