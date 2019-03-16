import math

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x < 0 :
        number = -x
    else:
        number = x
    finalNumber = 0
    while number > 0:
        digit  =  number % 10
        finalNumber = finalNumber * 10 + digit 
        number = int(number/10)
    if(finalNumber > ((1 <<31)-1) or finalNumber < (-1 <<31)) : return 0
    if x < 0:
        finalNumber = -finalNumber 
    return finalNumber   
    

num = reverse(123)
print(num)
#    1             2              3 
#   1 * 10^2      2 * 10^1      3 * 10^0
# 
# 
# 123/10 = 12 
# 


#  0000 0001 =>   1111 1111 


