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

# gui with tkinter
window = tk.Tk()
window.title('Generator')
window.geometry('350x500')
window.configure(bg='#D8D2C8', padx=20, pady=20)

# create a label for the entry
entry_label = tk.Label(window, text='Enter password length: ', font=('Arial', 20), bg='#D8D2C8', fg='#2F3A44')
entry_label.pack(side=tk.TOP, pady=10)

# create an entry for the password length
pass_entry = tk.Entry(window, width=20, font=('Arial', 20), bg='#D8D2C8', fg='#2F3A44', textvariable="")
pass_entry.pack(side=tk.TOP, pady=10)

# add validation to the entry
pass_entry.config(validate='focusout', validatecommand=(window.register(validate_length), '%P'), invalidcommand=invalid_length)

# create a label for the password
label = tk.Label(window, text='Password', font=('Arial', 20), bg='#D8D2C8', fg='#2F3A44')
label.pack(side=tk.TOP, pady=10)

# create a button to generator the password
button = tk.Button(window, text='Generate Password', font=('Arial', 20), bg='#D8D2C8', fg='#2F3A44', command=lambda: label.config(text=generate_password(pass_entry.get()), fg='#2F3A44'))
button.pack(side=tk.TOP, pady=10)

# start the main loop
window.mainloop()