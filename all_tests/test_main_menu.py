from main_menu_dic.main_menu import *
from main_menu_dic.main_menu_text import menu_option_text
from unittest.mock import patch, Mock, MagicMock


def test_displaying_the_name_of_the_game():
    displaying_the_name_of_the_game()


def test_selecting_and_input_option_from_user(monkeypatch):
    input_text = 'doesn\'t have matter'
    monkeypatch.setattr('builtins.input', lambda _: input_text)
    result = selecting_and_input_option_from_user(menu_option_text(), question_about_selected_option_text())
    assert input_text == result


def test_check_which_user_data_is_integer():
    samples = ['1', '23', 'x', '46', 'rj-45', '5gf']
    expected_result = [1, 23, None, 46, None, None]

    for counter in range(len(samples)):
        data_from_user = samples[counter]
        result = check_which_user_data_is_integer(data_from_user)
        assert result == expected_result[counter]


def test_checking_the_correctness_of_the_range():
    data_from_user = None
    range_from = 0
    range_to = len(menu_option_text())

    samples = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected_result = [None, None, 1, 2, 3, None, None, None, None, None, None, None]

    for counter in range(len(samples)):
        data_from_user = samples[counter]
        data_from_user = checking_the_correctness_of_the_range(range_from, range_to, data_from_user)

        assert data_from_user == expected_result[counter]
