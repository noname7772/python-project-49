from random import randint


def game_rules():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def ask_question():
    num = randint(0, 100)
    print('Question:', num)
    return num


def get_correct_answer(question):
    return 'yes' if is_prime_number(question) else 'no'


def is_prime_number(num):
    if num <= 1:
        return False
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return False
    return True
