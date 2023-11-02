from random import randint
import prompt


def game_rules():
    print('What number is missing in the progression?')


def get_answer():
    return prompt.string('Your answer: ')


def ask_question():
    min_length = 5
    max_length = 10
    progression_length = randint(min_length, max_length)
    step = randint(1, 10)
    start = randint(1, 10)
    stop = start + step * progression_length
    progression = range(start,
                        stop + 1,
                        step)
    missing_index = randint(0, progression_length - 1)
    print('Question:', end=' ')
    for index, number in enumerate(progression):
        if index == missing_index:
            print('..', end=' ')
            continue
        print(number, end=' ')
    print()
    return progression, missing_index


def get_correct_answer(question):
    progression, missing_index = question
    missing_number = tuple(progression)[missing_index]
    return str(missing_number)
