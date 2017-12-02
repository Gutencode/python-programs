## Program to print the natural numbers in a given range.

# Input range by the user.
begin_num = int(input("Enter the First Number : "))
end_num = int(input("Enter the Last Number : "))

# initialize counter
count = begin_num

print("\nNatural Number list from",begin_num,"to",end_num,"is :")

# while loop for printing natural numbers
while (count <= end_num):
    print(count)
    count += 1
