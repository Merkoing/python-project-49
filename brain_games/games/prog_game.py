import random

RULE = 'What number is missing in the progression?'


def get_progression():
    first_number = random.randint(0, 10)
    progression = [first_number]

    progression_size = random.randint(5, 10)
    step = random.randint(3, 11)

    while len(progression) < progression_size:
        next_number = progression[-1] + step
        progression.append(next_number)

    return progression


def game_data():
    progression = get_progression()

    last_index = len(progression) - 1
    random_index = random.randint(0, last_index)

    answer = progression[random_index]
    correct_answer = str(answer)

    progression[random_index] = '..'  # type: ignore
    question = ' '.join(map(str, progression))

    return question, correct_answer