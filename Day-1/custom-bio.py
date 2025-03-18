''' 
Creating a Bio Generator
We'll be creating a script that does the following:
• Takes user name and age and other details
• Prints a formatted bio message
'''

name = input("Enter your name: ")
age = input("Enter your age: ")
age = int(age)
age = age + 1
print(f"Hi, I'm {name} and m {age} years old.")

# another method to print
bio = f"Hello, my name is {name} and I am {age} years old."
print(bio)