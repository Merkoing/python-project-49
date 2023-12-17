import random

RULE = 'What is the result of the expression?'

MIN_NUMBER = 0
MAX_NUMBER = 20

def get_game_data():
    first_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    second_number = random.randint(MIN_NUMBER, MAX_NUMBER)

    operators = ['+', '-', '*']
    operator = random.choice(operators)

    question = f'{first_number} {operator} {second_number}'

    answer = 0

    if operator == '+':
        answer = first_number + second_number
    elif operator == "-":
        answer = first_number - second_number
    elif operator == "*":
        answer = first_number * second_number
    correct_answer = str(answer)

    return question, correct_answer
