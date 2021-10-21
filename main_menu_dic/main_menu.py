from extension_dic.view_text_in_console import set_input
from main_menu_dic.main_menu_text import *

range_from = 0
range_to = len(menu_option_text())


def displaying_the_name_of_the_game():
    set_input(game_name_text())


def selecting_and_input_option_from_user(options_text, question_about_selected_option_text):
    set_input(options_text, '\n')
    return input(question_about_selected_option_text)


def check_which_user_data_is_integer(data_from_user):
    try:
        data_from_user = int(data_from_user)
        return data_from_user
    except (ValueError, TypeError):
        set_input(error_wrong_data_type_text())
        return None


def checking_the_correctness_of_the_range(range_from, range_to, data_from_user):
    if range_from >= data_from_user or data_from_user > range_to:
        set_input(error_wrong_range_of_selected_data_text())
        return None
    else:
        return data_from_user


def go_to_the_selected_option(user_selection):
    if user_selection == 1:
        number_of_player()
        new_gameplay = New_match()
        return 1

    elif user_selection == 2:
        # score_board()
        return 2
    elif user_selection == 3:
        exit_game()


def main_menu_init():
    global range_from, range_to
    data_from_user = None

    while True:
        data_from_user = check_which_user_data_is_integer(
            selecting_and_input_option_from_user(menu_option_text(), question_about_selected_option_text()))

        if data_from_user is not None:
            data_from_user = checking_the_correctness_of_the_range(range_from, range_to, data_from_user)
            if data_from_user is not None:
                return data_from_user
