## Program to compute the smallest number among three numbers.

def smallest(a, b, c):
    """ This function takes three number and returns the smallest number """
    if (a<b and a<c):
        print("Smallest number is ",a)
    elif (b<c and b<a):
        print("Smallest number is ",b)
    else:
        print("Smallest number is ",c)
        
# Three numbers as input from user.
num_1 = int(input("Please enter the first number : "))
num_2 = int(input("Please enter the second number : "))
num_3 = int(input("Please enter the third number : "))

# function calling by passing arguments.
smallest(num_1,num_2,num_3)
