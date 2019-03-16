class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '' or len(s) == 1:
            return True
        
        s = s.lower()
        slist = list(s) 

        for i in range(len(slist)-1,-1,-1):
            ordI = ord(slist[i])
            if (ordI >= 48 and ordI <= 57) or (ordI >= 97 and ordI <= 122):
                continue
            else:
                slist.remove(slist[i])
        
        if len(slist) == 1:
            return True
        
        sPalin = slist[::-1]
        return slist == sPalin

    def isPalindrome2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        i = 0
        j = len(s) - 1 
        s = s.lower()
        while i<j : 

            while i<j and not s[i].isalnum():   
                i = i+ 1
    
            while i<j and not s[j].isalnum():  
                j = j- 1

            if s[i] == s[j]:   
                i = i + 1
                j = j - 1
            else:
                return False

        return True

sol = Solution()
print(sol.isPalindrome2('.,'))
