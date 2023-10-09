import random
from math import gcd

RULE = 'Find the greatest common divisor of given numbers.'


def game_data():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)

    question = f'{first_number} {second_number}'
    correct_answer = str(gcd(first_number, second_number))
    return question, correct_answer