import prompt


ROUND_MAX = 3


def play(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULE)
    incorrect_prompt = ' is wrong answer ;(. Correct answer was '

    for _ in range(ROUND_MAX):
        question, correct_answer = game.get_data()

        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer} {incorrect_prompt} {correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
