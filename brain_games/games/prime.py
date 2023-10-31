from random import randint

answer_yes = 'yes'
answer_no = 'no'


def game_rules():
    print(f'Answer "{answer_yes}" if given number is prime. Otherwise answer "{answer_no}".')


def ask_question():
    num = randint(0, 100)
    print('Question:', num)
    return num


def get_correct_answer(question):
    global answer_yes, answer_no
    return answer_yes if is_prime_number(question) else answer_no


def is_prime_number(num):
    for i in range(2, (num//2)+1):
        if num % i == 0:
            return False
        return True
