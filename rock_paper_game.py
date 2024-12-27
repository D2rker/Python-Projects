import random
rock = '''
    _________
___|     _____)
        (_____)
        (_____)
        (_____)
---|____(_____)
'''
paper = '''
    __________
___|     _____)_____
            ________)__
            ___________)
            __________)
---|____________)
'''
scissors = '''
    __________
___|     _____)____
            _______)
            __________)
         _____)
---|____(____)
'''
game_image = [rock, paper, scissors]
user_choice = int(input("What do you choice? type for 0 for rock, 1 for paper and 2 for scissors \n"))

if user_choice >= 3 or user_choice < 0:
    print("you type an invalid number, please type correct number.")
else:
    print(game_image[user_choice])
    computer_choice = random.randint(0,2)
    print("computer choose :")
    print(game_image[computer_choice])
    if user_choice == 0 and computer_choice == 2:
        print("you win")
    elif computer_choice == 0 and user_choice == 2:
        print("you lose")
    elif computer_choice > user_choice:
        print("you lose")
    elif user_choice > computer_choice:
        print("yu win")
    elif computer_choice == user_choice:
        print("its a drow")