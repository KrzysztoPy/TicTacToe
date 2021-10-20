from extension_dic.view_text_in_console import set_input
from main_menu_dic.main_menu_text import *

data_from_user = None


def displaying_the_name_of_the_game():
    set_input(game_name_txt())


def selecting_an_action_option():
    set_input(menu_option_txt(), '\n')
    return input(question_about_selected_option_txt())


def data_analysis_for_compilance_with_the_guidelines():
    user_data = check_which_user_data_is_integer(data_from_user)

    while True:
        if user_data or user_data == 0:
            if checking_the_correctness_of_the_range(user_input_data):
                return user_data


def check_which_user_data_is_integer(user_data):
    try:
        user_data = int(user_data)
        return user_data
    except (ValueError, TypeError):
        set_input(error_wrong_data_type_txt())
        return None


def checking_the_correctness_of_the_range(is_integer):
    if 0 < is_integer < 4:
        return is_integer
    else:
        set_input(error_wrong_range_of_selected_data())
        return None


def go_to_the_selected_option(user_selection):
    if user_selection == 1:
        new_gameplay = New_match()
        # new_gameplay.

        # draw_who_play_x_and_who_o()
        return 1

    elif user_selection == 2:
        # score_board()
        return 2
    elif user_selection == 3:
        exit_game()

# data_from_user = selecting_an_action_option()
# data_analysis_for_compilance_with_the_guidelines()
