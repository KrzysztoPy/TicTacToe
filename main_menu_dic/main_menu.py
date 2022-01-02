from another_func_dic.set_input_func import set_input
from main_menu_dic.main_menu_text import *


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
    if data_from_user < range_from or data_from_user > range_to:
        set_input(error_wrong_range_of_selected_data_text(range_from + 1, range_to))
        return None
    else:
        return data_from_user


def selecting_from_available_options(range_from, range_to, available_menu_option_str,
                                     question_about_selected_option_text):
    # range_from, range_to = range_from, range_to
    # data_from_user = None

    while True:
        selecting_from_available_options_inside_while_true(range_from, range_to, available_menu_option_str,
                                                           question_about_selected_option_text)


def selecting_from_available_options_inside_while_true(range_from, range_to, available_menu_option_str,
                                                       question_about_selected_option_text):
    selecting_from_available_options_inside_while_true()
    data_from_user = check_which_user_data_is_integer(
        selecting_and_input_option_from_user(available_menu_option_str, question_about_selected_option_text))

    if data_from_user is not None:
        data_from_user = checking_the_correctness_of_the_range(range_from, range_to, data_from_user)
        if data_from_user is not None:
            return data_from_user
