import random

RULE = 'What is the result of the expression?'


def game_data():
    first_number = random.randint(0, 20)
    second_number = random.randint(0, 20)

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
