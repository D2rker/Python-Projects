import random
print("Welcome to the pypssword generator")
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '=']
letters = int(input("how many letter would you like in your password? \n"))
numbers = int(input("how many number would you like in your password? \n"))
symbols = int(input("how many symbol would you like in your password? \n"))
password = ""
for char in range(1,letters + 1):
    random_char = random.choice(letter)
    password += random_char
for char in range(1,numbers + 1):
    random_char1 = random.choice(number)
    password += random_char1
for char in range(1,symbols + 1):
    random_char2 = random.choice(symbol)
    password += random_char2
print(f"your password is : {password}")
