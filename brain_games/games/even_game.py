from random import randint
from brain_games.cli import welcome_user


def is_even(number):
    return number % 2 == 0
   
def game():
    name = welcome_user()
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    correct_answers = 0
    while correct_answers < 3:
        number = randint(1, 100)
        print(f"Question: {number}")
        answer = input("Your answer: ")

        if (answer.lower() == "yes" and is_even(number)) or (answer.lower() == "no" and not is_even(number)):
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{answer}' is the wrong answer ;(. Correct answer was '{'yes' if is_even(number) else 'no'}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
