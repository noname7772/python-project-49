import prompt
from random import randint, choice


def game_rules():
    print('What is the result of the expression?')


def get_answer():
    return prompt.string('Your answer: ')


def ask_question():
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    operation = choice(['+', '-', '*'])
    print('Question:', f'{num1} {operation} {num2}')
    return num1, operation, num2


def get_correct_answer(question):
    num1, operation, num2 = question
    return str(is_correct(num1, operation, num2))


def is_correct(num1, operation, num2):
    if operation == '+':
        return num1 + num2
    if operation == '-':
        return num1 - num2
    if operation == '*':
        return num1 * num2
