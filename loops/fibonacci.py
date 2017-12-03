## Program to display the Fibonacci sequence up to n-th term where n is provided by the user

# input from the user
nth = int(input("Enter the number of terms upto which fibonacci series is to be shown : "))

# function to print and compute the next term in series
def fibonacci():
    first_term = 0
    second_term = 1
    
    # initialize counter variable
    counter = 0
    
    if (nth <= 0):
        print("Please enter the positive number")
    elif (nth == 1):
        print("Fibonacci sequence upto",nth,"term :",first_term)
    else:
        print("Fibonacci sequence upto",nth,"term :")
        while (counter <= nth):
            print(first_term, end = ",")
            # next term of the sequence
            next_term = first_term + second_term
            first_term = second_term
            second_term = next_term
            counter += 1

fibonacci()
