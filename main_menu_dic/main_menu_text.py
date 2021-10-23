def game_name_text():
    return '\nWelcome in simple Tic Tac Toe \n'


def menu_option_text():
    from_to = 0
    menu_list = ['1. Start', '2. Statistic', '3. Exit']
    return from_to, menu_list


def question_about_selected_option_text():
    return '\n Select option: '


def error_wrong_data_type_text():
    return '\n Incorrect data type. You can select only digt. Please try again.\n'


def error_wrong_range_of_selected_data_text():
    return '\n Incorrect data range. You can selected option from range {} to {}. Please try again. \n'.format(1,
                                                                                                               menu_option_text().__len__())