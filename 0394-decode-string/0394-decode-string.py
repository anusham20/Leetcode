class Solution:

    def decodeString(self, s: str) -> str:
        stack = []
        currS = ""
        currNum = 0

        for char in s:
            if char.isdigit():
                currNum = currNum * 10 + int(char)
            
            elif char == "[":
                stack.append((currS, currNum))
                currS = ""
                currNum = 0

            elif char == "]":
                prevS, prevNum = stack.pop()
                currS = prevS + (currS * prevNum)
            
            else:
                currS += char

        return currS

        