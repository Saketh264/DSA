class Solution:
    def interpret(self, command: str) -> str:
        strs=""
        for i in range(len(command)):
            if command[i].isalpha(): strs+=command[i]
            if command[i]=='(' and command[i+1]==')': strs+="o"
        return strs

        