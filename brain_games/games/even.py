from random import randint

max_score = 3
rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(random_number: int):
    return True if random_number % 2 == 0 else False


def run_game():
    score = 0
    random_number = randint(0, 100)
    question = f'Question:{random_number}'
    while score < max_score:
        target_result = 'yes' if is_even(random_number) else 'no'
        score += 1
    return question, target_result

