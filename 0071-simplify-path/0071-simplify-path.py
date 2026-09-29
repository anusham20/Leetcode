class Solution:
    def simplifyPath(self, path: str) -> str:
        arrStr = path.split("/")
        result = "/"
        resultArr = []
        for element in arrStr:
            if element == "" or element == ".": continue
            if element == "..": 
                if resultArr != []:
                    resultArr.pop()
            else: resultArr.append(element)

        for dir in resultArr:
            result = result + dir + "/"

        if result == "/": return result

        return result[:-1]