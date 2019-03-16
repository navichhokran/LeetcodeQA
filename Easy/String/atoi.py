import sys

class Solution:
    def myAtoi(self, str: str) -> int:
        
        str = str.strip()
        INT_MAX:int  = (1<<31)-1
        INT_MIN:int  = -1<<31
        isSigned: bool = (str[0] =='-' or str[0] == '+') if len(str)>0 else 0
        resultant: str = ''

        
        if str == '' or str == None :
            return 0
        elif isSigned and len(str) == 1:
            return 0
        elif isSigned and not str[1].isdigit():
            return 0
        elif not isSigned and not str[0].isdigit():
            return 0
        
        if isSigned:
            resultant = resultant + str[0]
            str = str[1:]
        
        for char in str:
            if char.isdigit():
                resultant =  resultant + char
                if int(resultant) > INT_MAX:
                    return INT_MAX
                elif int(resultant) < INT_MIN:
                    return INT_MIN
            else:
                break

        return int(resultant)


sol = Solution()

args = sys.argv
print(sol.myAtoi(args[1]))