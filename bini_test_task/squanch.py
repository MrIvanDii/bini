import os
import shutil
from datetime import date
from random import choice

folder_name = 'squanch'
if os.path.exists(f'{os.getcwd()}/{folder_name}/{date.today()}_{folder_name}.txt'):
    shutil.rmtree(f'{os.getcwd()}/{folder_name}')

os.mkdir(f'{os.getcwd()}/{folder_name}')
os.chdir(f'{os.getcwd()}/{folder_name}')

with open(f'{date.today()}_{folder_name}.txt', 'w') as file:
    word = ''
    for char in folder_name:
        random_char = choice(folder_name)
        word += random_char
        folder_name = folder_name.replace(random_char, '')

    file.write(f"Let's {word}")
