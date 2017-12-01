## Program to compute the grade from given percentage.

def grade(percent):
    
    """ This function takes the percentage as input and returns the relevant grade. """
    
    if (percent > 100):
        print("Please enter the correct obtained percentage")
    elif (percent >= 90):
        return("A")
    elif (percent >= 80):
        return("B")
    elif (percent >= 70):
        return("C")
    elif (percent >= 60):
        return("D")
    elif (percent >= 50):
        return("E")
    elif (percent >= 40):
        return("F")
    elif (percent >= 30):
        return("G")
    else:
        return("Fail")

# Input from the user.
percent = float(input("Please enter the obtained percentage : "))

# Function get called and the statement print the corresponding returned grade.
print("You earned",grade(percent),"grade")
