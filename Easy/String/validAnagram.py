from  collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t): 
            return False
        
        abc = 'abcdefghijklmnopqrstuvwxyz'
        charCounts = 0
        charCountt = 0 

        for char in abc:
            charCounts = s.count(char)
            charCountt = t.count(char)
            if(charCounts != charCountt):
                return False
            
        return True
    
    def isAnagram2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t): 
            return False
        
        setS = set(s)

        for char in setS:
            if s.count(char) != t.count(char):
                return False
            
        return True


sol = Solution()
print(sol.isAnagram2('anagram','nagaram'))
