## Program to determine whether the given number is an Armstrong number or not.

# input from the user
print("Program to determine whether the given number is an Armstrong number or not !")
num = int(input("Enter the number : "))

# function to determine the order of the given number
def orderOf(n):
    """ function takes integer as input and returns order of that number """
    
    # initialize the variable odr for order of number
    odr = 0
    
    while (int(n) != 0):
        n = n / 10
        odr = odr + 1
        
    return (odr)

# function to check whether number is Armstrong number or not
def isArmstrong(number):
    """ function takes integer as input and returns the logical result (true or false) """
    
    # initialize the varable sum
    sum = 0
    
    while (int(number) != 0):
        var_rem = number % 10
        var_num = var_rem ** orderOf(num)
        sum = sum + var_num
        number = number // 10
    
    if (num == sum):
        print("Given number",num,"is an Armstrong number")
    else:
        print("Given number",num,"is not an Armstrong number")

# calling function
isArmstrong(num)
