# import libraries
import tkinter as tk
import random
import string

# generate password functions
def generate_password(length):
    if length.isdigit():
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for _ in range(int(length)))
        return password
    else:
        return 'Invalid length'

# validate length function
def validate_length(text):
    if text == '':
        return True
    elif text.isdigit():
        return int(text) > 0
    else:
        return False

# invalid length function
def invalid_length():
    label.config(text='Invalid length', fg='red')