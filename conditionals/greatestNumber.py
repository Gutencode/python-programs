## Program to compute the greatest number among the four numbers.

def greatestNumber(a, b, c, d):
    """ This function takes four numbers as arguments and returns greatest number  """
    if (a>b and a>c and a>d):
        return a
    elif (b>a and b>c and b>d):
        return b
    elif (c>a and c>b and c>d):
        return c
    else:
        return d

# Four numbers as input from user.
num_1 = int(input("Enter the First number : "))
num_2 = int(input("Enter the Second number : "))
num_3 = int(input("Enter the Third number : "))
num_4 = int(input("Enter the Forth number : "))

# function calling and printing the value that is returned by the function
result = print("Greatest number is",greatestNumber(num_1, num_2, num_3, num_4))
