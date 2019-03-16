class Solution:
    def longestCommonPrefix(self, strs) -> str:
        
        finalStr = ''
        k = 0

        if len(strs) < 1:
            return ''
        elif len(strs) == 1 :
            return strs[0]

        while k < min([len(d) for d in strs]):
            prefix = strs[0][k]
            for element in strs:
                if prefix != element[k] :
                    return finalStr
            finalStr = finalStr + prefix
            k+=1

        return finalStr    

    def longestCommonPrefix2(self, strs) -> 'str':
            if not strs:
                return ''
            
            s1 = min(strs)
            s2 = max(strs)

            print(s1,s2)
            
            for i, v in enumerate(s1):
                if v != s2[i]:
                    return s1[:i]
                        
            return s1

sol = Solution()
print(sol.longestCommonPrefix2(['doggy','degpark','dogdggydogparkeverywhereinArbors']))


