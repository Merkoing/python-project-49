import random

RULE = 'What number is missing in the progression?'

MIN_INITIAL_TERM = 0
MAX_INITIAL_TERM = 10
MIN_PROGRESSION_LENGTH = 5
MAX_PROGRESSION_LENGTH = 10
MIN_DIFFERENCE = 1
MAX_DIFFERENCE = 10  


def generate_progression(initial_term, length, difference):
    return [initial_term + i * difference for i in range(length)]


def generate_question_and_answer(progression, hidden_index):
    progression_with_placeholder = progression[:]
    progression_with_placeholder[hidden_index] = '..'
    question = ' '.join(map(str, progression_with_placeholder))
    correct_answer = str(progression[hidden_index])
    return question, correct_answer


def get_data():
    initial_term = random.randint(MIN_INITIAL_TERM, MAX_INITIAL_TERM)
    progression_length = random.randint(MIN_PROGRESSION_LENGTH, MAX_PROGRESSION_LENGTH)
    difference = random.randint(MIN_DIFFERENCE, MAX_DIFFERENCE)
    progression = generate_progression(initial_term, progression_length, difference)

    hidden_index = random.randint(0, len(progression) - 1)

    return generate_question_and_answer(progression, hidden_index)
