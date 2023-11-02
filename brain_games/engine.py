import prompt
from brain_games.cli import welcome_user


def run_game(module):
    user_name = welcome_user()
    module.game_rules()
    question_count = 3
    for i in range(question_count):
        question = module.ask_question()
        answer = get_answer()
        if not is_correct_answer(module, question, answer):
            correct = module.get_correct_answer(question)
            game_over(user_name, answer, correct)
            break
        print('Correct!')
    else:
        congratulations(user_name)


def game_over(user_name, answer, correct):
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}')")
    print(f"Let's try again, {user_name}!")


def is_correct_answer(module, question, answer):
    correct = module.get_correct_answer(question)
    return correct == answer


def get_answer():
    return prompt.string('Your answer: ')


def congratulations(user_name):
    print(f'Congratulations, {user_name}!')
