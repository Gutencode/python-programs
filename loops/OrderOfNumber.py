## Program to determine the order of the given number

# Input number from user
number = int(input("Enter the number : "))

# Function to calculate the order of the number
def order(num):
    """This function takes integer as an input and returns order of that number when called"""
    # Initialize the variable to store the number of digits
    digit = 0
    while (int(num) != 0):
        num = num / 10
        digit += 1
    return(digit)

print("Order of the number",number,":",order(number))
