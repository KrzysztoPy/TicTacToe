def how_many_player_text():
    from_to = 0
    options = ['1. Player vs Player', '2. Player vs Computer']
    return from_to,options


def set_player_name_text(current_player):
    return '\nSet nama for {0}: '.format(current_player)


def rules_for_creating_player_name_text():
    return '\nIn creating a player name can\'t be use space and set an empty field. Instead use space you can use bottom underline = \'_\'.  '


def request_for_the_user_name_text(player_name):
    return ' Please enter name {}: '.format(player_name)


def confirmation_name_selection_text(name):
    return ' If you confirm that you have chosen a {} name press '.format(name)


def selected_option_text():
    return 'Selected option: '


def player_name_is_empty_text():
    return 'Player name is empty. Please try again.'


def converted_all_space_to_underline_text():
    return ' Converted all space to underline.'


def want_keep_the_player_name_text(new_player_name):
    return 'You confirm selected \' {0} \' name? Yes press button y or Y, if you want change name press button  n or N ? '.format(
        new_player_name)


def invalid_press_button_text():
    return '\nYou pressed invalid key. If you confirm  player name selected press \'y\' or \'Y\' button, if you want change name press \'n\' or \'N\' button. Please try again.'
