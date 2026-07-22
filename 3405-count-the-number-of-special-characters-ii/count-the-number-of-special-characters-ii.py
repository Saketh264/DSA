class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lastLower={}
        firstUpper={}
        for i, ch in enumerate(word):
            if ch.islower():
                lastLower[ch]=i
            else:
                if ch not in firstUpper:
                    firstUpper[ch]=i
        c=0
        for ch in lastLower:
            up=ch.upper()
            if up in firstUpper and lastLower[ch] < firstUpper[up]:c+=1
        return c