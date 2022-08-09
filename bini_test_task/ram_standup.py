import sys
import random
from random import choice
import ramapi
from ramapi import Base
from ramapi import Character
import json
from jokeapi import Jokes
import asyncio
import time

def decision():
    input("\nWould you like to continue?\nPress 'Enter': ")


#number of web pages with characters
char_pgs = ramapi.Character.get_all()['info']['pages']

#number of all characters
num_all_char = 826

# Get_Joke
async def make_joke():
    j = await Jokes()
    joke = await j.get_joke()
    if joke['type'] == 'single':
        return joke['joke']
    else:
        first_part = (joke['setup'])
        second_part = (joke['delivery'])
        return first_part, second_part

rand_joke = asyncio.run(make_joke())

# Get_The_Random_Characters
list_of_guests = []
for one_of_seven_char in range(0, 7):
    id_of_random_char = random.randint(1, num_all_char)
    picked_chracter = ramapi.Character.get(id_of_random_char)['name']
    list_of_guests.append(picked_chracter)

#Host_of_the_show
host_of_the_show = ramapi.Character.get(random.randint(1, num_all_char))['name']

#Greetings_and_presenting_guests
print(f'{host_of_the_show}: - Wubba Lubba Dub Dub !!!')
time.sleep(2)
print(f'{host_of_the_show}: - Welcome to our Stand - UP show!')
time.sleep(2)
print(f'{host_of_the_show}: - Seven great comedians are performing for you today !!!')
time.sleep(2)
print(f'{host_of_the_show}: - Here they are: ')
for name in list_of_guests:
    time.sleep(1)
    print(f'{host_of_the_show}: - {name}.')
time.sleep(2)
print(f'\n{host_of_the_show}: - Are you excited?')
time.sleep(2)
print('\nWould you like to continue?')
decision_1 = input('press "Enter": _')

#Guests_presentation_one_by_one
next_guest = 'first'
for name in list_of_guests:
    print(f'\n{host_of_the_show}: - Meet our {next_guest} guest!  {name} !')
    next_guest = 'next'
    time.sleep(2)

    #Joke_Jrom_Guest
    rand_joke = asyncio.run(make_joke())
    if len(rand_joke) == 2:
        print(f'\n{name}: - {rand_joke[0]}')
        time.sleep(2)
        print(f'{name}: - {rand_joke[1]}')
        time.sleep(2)
        decision()
    else:
        print(f'{name}: - {rand_joke}')
        time.sleep(2)
        decision()

print(f'{host_of_the_show}: - It was a night of unforgettable humor!\nThanks to our guests!')
print(f"{host_of_the_show}: - And now, dear audience, let's vote for the best comedian of the evening!")
print(f"{host_of_the_show}: - And... the winner is...")
time.sleep(3)
print(f'{host_of_the_show}: - Boom! Big reveal! And the winner is {choice(list_of_guests)}!!!')
print(f'{host_of_the_show}: - Thank you, dear audience, for your participation and see you soon again!')
decision()
sys.exit(0)
