class Solution:
    def countAndSay(self, n: int) -> str:
        s = ['1']
        newS = []

        for _ in range(1,n):
            i = 0
            while i < len(s):
                count = 1 
                j = i 
                while j < len(s)-1 and s[j] == s[j+1]  : 
                    count += 1
                    j += 1
                newS.append(str(count))
                newS.append((s[i]))
                i = i + count
            s = newS
            newS = []        
        return ''.join(s)



sol = Solution()

print(sol.countAndSay(1))
