class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        x=sentence.split()
        for i,word in enumerate(x):
            if word.startswith(searchWord): return i+1
        return -1