from main_menu_dic.main_menu import *


def test_displaying_the_name_of_the_game():
    displaying_the_name_of_the_game()


def test_check_which_user_data_is_integer():
    samples = ['1', '23', 'x', '46', 'rj-45', '5gf']
    expected_result = [1, 23, None, 46, None, None]

    for counter in range(len(samples)):
        result = check_which_user_data_is_integer(samples[counter])
        assert result == expected_result[counter]
