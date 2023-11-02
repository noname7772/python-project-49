import prompt
from random import randint


def game_rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def get_answer():
    return prompt.string('Your answer: ')


def ask_question():
    num = randint(0, 100)
    print('Question:', num)
    return num


def get_correct_answer(question):
    return 'yes' if is_even_number(question) else 'no'


def is_even_number(num):
    return num % 2 == 0
