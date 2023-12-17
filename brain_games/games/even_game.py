import random

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'

MIN_NUMBER = 0
MAX_NUMBER = 100

def is_even(number):
    return number % 2 == 0

def get_game_data():
    question = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if is_even(question) else 'no'

    return question, correct_answer
