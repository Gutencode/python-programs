## Program to compute the given number is even or odd

def EvenTest(number):
    """ This function takes number as an input and returns the value as even or odd. """
    if (number % 2 == 0):
        return ("Even")
    else:
        return ("Odd")
    

# Take the number as inut from user.
number = int(input("Enter the number (any integer) : "))

# Calling function by passing an argument and Printing the value.
print("Given number is",EvenTest(number))
