'''
.make a calculator
.ask for two numbers
.ask for operation
.Print results
'''
from arithmetic_operations import add, diff

try:

    number_1 =int(input("Enter your first number :"))
    number_2 =int(input("Enter your second number :"))

    operate = input("Enter operation: + for sum, - for difference, * for multiply, / for division ")

    if operate == "+":
        result = number_1 + number_2
    elif operate == "-":
        result= number_1 - number_2
    else:
        result = "Invalid Operation"

    print(f"Result :{result}")

except ValueError:
    print ("Invalid input")
except NameError:
    print("Invalid operation" )
else:
    print ("Operation performed successfully")
finally:
    print ("End of program"),