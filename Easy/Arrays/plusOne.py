class PlusOne():
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]

        [9,9,9,9]
        """

        i = len(digits)-1

        while i >= 0:
            if digits[i] != 9 :
                digits[i] = digits[i] + 1
                break  
            elif i!=0 : 
                digits[i] = 0
            else:
                digits[i] = 0
                digits.insert(0,1)
            i = i-1    
        return digits

digits = [9,9,9]
plusOne = PlusOne()
modifiedDigits = plusOne.plusOne(digits)

print(modifiedDigits)