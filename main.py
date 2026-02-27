# import libraries
from tkinter import *
import secrets
import string

# generate password functions
def generate_password(length):
    if length.isdigit():
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(chars) for _ in range(int(length)))
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
    word.set("Invalid length")

# gui with tkinter
window = Tk()
window.title('Generator')
window.geometry('350x500')
window.configure(bg='#D8D2C8', padx=20, pady=20)

# create a label for the entry
entry_label = Label(window, text='Enter password length', font=('Arial', 20), bg='#D8D2C8', fg='#2F3A44')
entry_label.pack(side=TOP, pady=10)

# create an entry for the password length
pass_entry = Entry(window, width=20, font=('Arial', 20), bg='#D8D2C8', fg='#2F3A44')
pass_entry.pack(side=TOP, pady=10)

# add validation to the entry
pass_entry.config(validate='focusout', validatecommand=(window.register(validate_length), '%P'), invalidcommand=window.register(invalid_length))

# create variable to store the password
word = StringVar(window)

# function to generate and display password
def generate():
    password = generate_password(pass_entry.get())
    word.set(password)

# create a button to generator the password
button = Button(window, text='Generate', font=('Arial', 20), bg='#D8D2C8', fg='#2F3A44', command=generate)
button.pack(side=TOP, pady=10)

# create a entry for the password
entry = Entry(window, width=20, state='readonly', textvariable=word, font=('Arial', 20), bg='#D8D2C8', fg='#2F3A44')
entry.pack(side=TOP, pady=10)

# start the main loop
window.mainloop()