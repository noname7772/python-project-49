from random import randint
import prompt


def game_rules():
    print('Find the greatest common divisor of given numbers.')


def get_answer():
    return prompt.string('Your answer: ')


def ask_question():
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    print('Question:', f'{num1} {num2}')
    return num1, num2


def get_correct_answer(question):
    num1, num2 = question
    return str(is_correct(num1, num2))


def is_correct(num1, num2):
    if num1 > num2:
        x = num2
    else:
        x = num1
    for i in range(1, x + 1):
        if (num1 % i == 0) and (num2 % i == 0):
            x = i
    return x
