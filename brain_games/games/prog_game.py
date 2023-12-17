import random

RULE = 'What number is missing in the progression?'

MIN_START_NUMBER = 0
MAX_START_NUMBER = 10
MIN_PROG_SIZE = 5
MAX_PROG_SIZE = 10
MIN_STEP = 1
MAX_STEP = 10


def generate_progression(start, length, step):
    return [start + i * step for i in range(length)]


def generate_question_and_answer(progression, hidden_index):
    progression_with_placeholder = progression[:]
    progression_with_placeholder[hidden_index] = '..'
    question = ' '.join(map(str, progression_with_placeholder))
    correct_answer = str(progression[hidden_index])
    return question, correct_answer


def get_game_data():
    start_number = random.randint(MIN_START_NUMBER, MAX_START_NUMBER)
    progression_size = random.randint(MIN_PROG_SIZE, MAX_PROG_SIZE)
    step = random.randint(MIN_STEP, MAX_STEP)
    progression = generate_progression(start_number, progression_size, step)

    hidden_index = random.randint(0, len(progression) - 1)

    return generate_question_and_answer(progression, hidden_index)
