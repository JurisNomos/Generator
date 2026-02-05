# main.py
import string
import random

# get password length 
length = int(input('Enter password length: '))
print()

# password setting menu
print('Generator:\n1. Digits\n2. Letters\n3. Special characters\n4. Exit\n')

characters = ""

# set password
while True:
    try:
        choice = int(input('Pick a number: '))
        print()

        if choice == 1:
            # add digits to characters
            characters += string.digits
        
        elif choice == 2:
            # add letters to characters
            characters += string.ascii_letters
        
        elif choice == 3:
            # add special characters to characters
            characters += string.punctuation
        
        elif choice == 4:
            break

        else:
            print('Invalid option, try again\n')
    except:
        print('Invalid input, try again\n')

password = []

for index in range(length):
    # random choice characters
    choice_characters = random.choice(characters)

    password.append(choice_characters)

    # random shuffle password list
    random.shuffle(password)

print('The random password is ' + ''.join(password))