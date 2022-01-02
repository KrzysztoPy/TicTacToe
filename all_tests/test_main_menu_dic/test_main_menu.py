import main_menu_dic.main_menu
from main_menu_dic.main_menu import selecting_and_input_option_from_user, check_which_user_data_is_integer, \
    checking_the_correctness_of_the_range, selecting_from_available_options

from random import randint
from unittest import mock


def test_selecting_and_input_option_from_user(monkeypatch):
    samples_menu = (('\n1.Start', '2.Stop'), ('\n0.Play',), [])
    sample_question = ('Which option selected',) * 3

    for elem in zip(samples_menu, sample_question):
        monkeypatch.setattr('builtins.input', lambda _: sample_question[1])

        result = selecting_and_input_option_from_user(elem[0], elem[1])
        assert result == elem[1]


def test_check_which_user_data_is_integer():
    samples = ['z', '7', 'ww', '89', 'FF', '0b111']
    expected_result = [None, 7, None, 89, None, None]

    for elem in zip(samples, expected_result):
        result = check_which_user_data_is_integer(elem[0])
        assert result == elem[1]


def test_checking_the_correctness_of_the_range():
    samples_from = (0, 4, 74)
    samples_to = (1, 12, 978)
    samples_data_from_user_appropriate_range = [(i[0], i[1], i[1] // 2) for i in zip(samples_from, samples_to)]
    samples_data_from_user_wrong_range = [(i[0] - 1, i[1] + 1, randint(-1000, (i[0] - 2)), randint(i[1] + 2, +1000))
                                          for i in zip(samples_from, samples_to)]

    for elem in samples_data_from_user_appropriate_range:
        for counter in range(len(elem)):
            result = checking_the_correctness_of_the_range(elem[0], elem[1], elem[counter])
            assert result == elem[counter]

    for elem in samples_data_from_user_wrong_range:
        for counter in range(len(elem)):
            result = checking_the_correctness_of_the_range(elem[0] + 1, elem[1] - 1, elem[counter])
            assert result is None


def test_selecting_from_available_options_inside_while_true():

    with 'main_menu_dic.main_menu.check_which_user_data_is_integer' as mock_check_which_user_data_is_integer:
        mock_check_which_user_data_is_integer = None


    samples_appropriate_data = []
