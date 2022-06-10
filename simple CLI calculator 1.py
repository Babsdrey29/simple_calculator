#my program for simple calculator

#function to add
def add(num1, num2):
    return num1 + num2
#function to subtract
def subtract(num1, num2):
    return num1 - num2
#function to multiply
def multiply(num1, num2):
    return num1 * num2
#function to divide
def divide(num1, num2):
    return num1 / num2
#modulus function
def modulus(num1, num2):
    return num1 % num2

print("Select operation to use.")
print("+")
print("-")
print("*")
print("/")
print("%")

#user inputs 
while True:
    choice = input("enter operation to use;")
    if choice in ("+", "-", "*", "/", "%"):
        num1 = int(input("enter first number;"))
        num2 = int(input("enter second number;"))
    else:
        print("wrong answer")
    if choice == "+":
        sum = int(num1) + int(num2)
        print(sum)
    elif choice == "-":
        Difference = int(num1) - int(num2)
        print(Difference)
    elif choice == "*":
        product = int(num1) * int(num2)
        print(product)
    elif choice == "/":
        division = int(num1) / int(num2)
        print(division)
    elif choice == "%":
        modulu = int(num1) % int(num2)
        print(modulu)
         # check if user wants to continue
        # break the while loop if user doesn't want to continue
    next_calculation = input("continue? (yes/no): ")
    if next_calculation == "no":
          break
    