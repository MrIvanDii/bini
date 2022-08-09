import os
from datetime import date
from random import choice

current_date = date.today()
name_of_txtfile = f'{current_date}_squanch.txt'
path = os.getcwd()
directory = list(os.walk(path))
folder_name = 'squanch'

for dirs, folders, files in directory:
    if folder_name not in folders:
        os.mkdir(folder_name)
    else:
        print('folder "squanch" already exists')
    path = os.path.join(dirs, folder_name)
    break

os.chdir(path)

with open(f'{name_of_txtfile}', 'w') as file:
    word = ''
    for char in folder_name:
        random_char = choice(folder_name)
        word += random_char
        folder_name = folder_name.replace(random_char, '')

    file.write(f"Let's {word}")