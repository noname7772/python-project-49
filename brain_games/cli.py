import prompt


def welcome_user(game_start=""):
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name?")
    print(f"Hello, {user_name}!")
    return user_name

