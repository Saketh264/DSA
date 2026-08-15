class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        tar=ord(target)
        for i in letters:
            if ord(i)>tar:
                return i
        return letters[0]