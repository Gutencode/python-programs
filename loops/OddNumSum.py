## Program to print the sum of odd numbers in a user defined range without for loop.

# input from the user
first_num = int(input("Enter the First Number : "))
last_num = int(input("Enter the last Number : "))

def add(a,b):
    """ This function takes two numbers as input and returns sum of those numbers as output """
    return(a + b)
    
# initialize counter and sum
sum = 0
count = first_num

# while loop
while (count <= last_num):
    if (count % 2 != 0):
        sum = add(count, sum)
        count += 1
    else:
        count += 1
        
print("The sum of odd numbers between",first_num,"and",last_num,"is :",sum)
