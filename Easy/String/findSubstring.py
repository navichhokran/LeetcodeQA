class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle == '':
           return 0

        if len(haystack) < len(needle):
            return -1

        
        for i in range(len(haystack) - len(needle)+1) :
            break1 = False
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    break1= True
                    break

            if not break1:
                return i
        return -1         



haystack = 'abcd'
needle = 'cd'
print(needle in haystack)