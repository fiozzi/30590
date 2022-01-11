# Wordle
# a game with 5 letter words

import random
import configparser
from datetime import datetime, timedelta
from enum import  Enum
import string

WORDLENGTH = 5

# reading configuration file
config = configparser.ConfigParser()
config.read('wordle.ini')
HOURS_DELAY = config['DEFAULT']['HoursDelay']
LAST_TIME_USED = config['DEFAULT']['LastTimeUsed']
LAST_TIME_FORMAT = config['DEFAULT']['LastTimeFormat']
LEVEL = config['DEFAULT']['Level'].upper()
MAX_GUESSES = int(config['DEFAULT']['maxguesses'])

alphabet = string.ascii_lowercase

class Level(Enum):
    NORMAL = 1
    EASY = 2
    HARD = 3

def find_a_word():
    return 'Iozzi'

def confirm_play():
    return True

def get_guess(level):
    return random.choices(alphabet, k = WORDLENGTH)

def is_in_wordlist(guess):
    return True

def compare(guess, word_to_guess):
    return [0] * WORDLENGTH

def display_result(result):
    print(result)

def display_status(status, LEVEL):
    if LEVEL == Level['HARD']:
        disp_string = ''
        for letter in status:
            if letter:
                disp_string += '_ '
            else:
                disp_string += letter + ' '
    else:
        disp_string = '_ ' * WORDLENGTH
    return disp_string.strip()


elapsed_time = datetime.now() - datetime.strptime(LAST_TIME_USED, LAST_TIME_FORMAT)
ok_to_play = ( elapsed_time > int(HOURS_DELAY)*timedelta(hours=1))
if ok_to_play:
    print(f'{elapsed_time} had passed so you can play!')
    # confirm()
    if confirm_play():
        word_to_guess = find_a_word()
        print(word_to_guess)
        # current status
        # contains the "green" letters, those at the right place.
        # useful only with HARD level
        status = [''] * WORDLENGTH
        # main loop
        for i in range(MAX_GUESSES):
            display_status(status, LEVEL)
            while True:
                guess = get_guess(LEVEL)
                guess = print(guess)
                if not is_in_wordlist(guess):
                    print('"{guess} not in wordlist!')
                    if add_wordlist(guess):
                        print(f'{guess} added to word list')
                        break
                else:
                    break
            result = compare(guess = guess, word_to_guess = word_to_guess)
            display_result(result)
            if guess == word_to_guess:
                print(f'You made it in {i+1} guess(es)! Good job!')
        print(f'Sorry, you had only {MAX_GUESSES} guesses. The hidden word was {word_to_guess}.')
else:
    next_time = datetime.now() - elapsed_time + int(HOURS_DELAY)*timedelta(hours=1)
    print(f'Too early. You must wait until: {next_time}')
