#  1

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else: 
    print("The number is negative. ")


# 2

def numbers():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    # largest
    if num1 >= num2 and num1 >= num3:
        largest = num1
    elif num2 >= num1 and num2 >= num3:
        largest = num2
    else:
        largest = num3

    # smallest
    if num1 <= num2 and num1 <= num3:
        smallest = num1
    elif num2 <= num1 and num2 <= num3:
        smallest = num2
    else: 
        smallest = num3
    # output
    print(f"The smallest number is {smallest}. the largest number is {largest}.")
# calling function  
numbers()

# 3

def leap_year_checker():

    year = int(input("Please enter a year: "))
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else: 
        print(f"{year} is not a leap year.")

leap_year_checker()