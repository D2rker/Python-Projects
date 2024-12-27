import random
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_lists = [
'blitz',
'blizzard',
'boggle',
'bookworm',
'boxcar',
'boxful',
'buckaroo',
'buffalo',
'buffoon',
'buxom',
'buzzard',
'buzzing',
'buzzwords',
'caliph',
'cobweb',
'cockiness',
'croquet',
'crypt',
'curacao',
'cycle',
'daiquiri',
'dirndl',
'disavow',
'dizzying',
'duplex',
'joking',
'jovial',
]



print(logo)
game_is_finished = False
lives = 6

choosen_word = random.choice(word_lists)
word_length = len(choosen_word)

display = []
for _ in range(word_length):
    display += "_"

while not game_is_finished:
    guess = input("guess a  letter").lower()
    if guess in display:
        print(f"you have already guessed {guess}")
    for position in range(word_length):
        letter = choosen_word[position]
        if letter == guess:
            display[position] = letter

    print(stages[lives])

    if guess not in choosen_word:
        print(f"you guessed {guess}, that's not in the word. you lose a life")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("you lose")

    print(f"{' '.join(display)}")

    if not "_" in display:
        game_is_finished = True
        print("you win")







