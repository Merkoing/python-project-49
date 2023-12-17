import random
import math

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


MIN_NUMBER = 0
MAX_NUMBER = 50


def is_prime(number):
    if number <= 1:
        return False
    number_sqrt = int(math.sqrt(number))
    divisors = range(2, (number_sqrt + 1))
    for element in divisors:
        if number % element == 0:
            return False
    return True


def get_game_data():
    question = random.randint(MIN_NUMBER, MAX_NUMBER)

    if is_prime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer
