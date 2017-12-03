## Program to print the sum of natural numbers

# Input number range by user
print("You will get the sum of natural numbers in a range")

initial_num = int(input("Enter the First Natural Number : "))
final_num = int(input("Enter the Last Natural Number : "))

# Function to perform addition
def add(a, b):
    """ This function takes two natural numbers as input and returns the addition of two numbers """
    result = a + b
    return(result)

# initialize counter 'count' and 'sum' for while loop
sum = 0
count = initial_num

# while loop
while (count <= final_num):
    sum = add(count, sum)
    count += 1

print("The sum is :",sum)
