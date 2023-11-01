import prompt
from random import randint

answer_yes = 'yes'
answer_no = 'no'


def game_rules():
    print(f'Answer "{answer_yes}" if the number is even, otherwise answer "{answer_no}".')


def get_answer():
    return prompt.string('Your answer: ')


def ask_question():
    num = randint(0, 100)
    print('Question:', num)
    return num


def get_correct_answer(question):
    global answer_yes, answer_no
    return answer_yes if is_even_number(question) else answer_no


def is_even_number(num):
    return num % 2 == 0


