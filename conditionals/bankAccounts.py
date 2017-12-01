## Program to compute the required Minimum balance per month in a bank account.

def accountBalance(residenceType, age, cardType):
    
    if (residenceType == "Urban" and age < 18):
        if (cardType == "Silver"):
            return("Rs 1000")
        elif (cardType == "Gold"):
            return("Rs 1500")
        else:
            return("Rs 2000")
        
    elif (residenceType == "Urban" and age >= 18):
        if (cardType == "Silver"):
            return("Rs 1500")            
        else:
            if (cardType == "Gold"):
                return("Rs 2000")
            else:
                return("Rs 2500")
                
    elif (residenceType == "Non Urban" and age < 18):
        if (cardType == "Silver"):
            return("Rs 800")
        elif (cardType == "Gold"):
            return("Rs 1200")
        else:
            return("Rs 1600")
            
    else:
        if (cardType == "Silver"):
            return("Rs 1000")
        else:
            if (cardType == "Gold"):
                return("Rs 1500")
            else:
                return("Rs 2000")
            


name = input("Please tell me you name : ")
print("Hello",name)

residenceType = input("Plese enter the type of your residence, 'Non Urban' or 'Urban': ")
age = int(input("Please enter your age : "))
cardType = input("Tell the type of debit card you need, \"Silver, Gold or Global\" : ")


# Calling function to evaluate the minimum balance required in account.
print("Minimum balance required in account per month is :", accountBalance(residenceType, age, cardType))
