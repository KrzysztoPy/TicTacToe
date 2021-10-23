from extension_dic.player_class import Player
from menu_options_dic.exit_game_dic import exit_game


def go_to_the_selected_option(user_selection):
    switch = {
        1: nummber_of_player,
        2: lambda: 2,
        3: exit_game
    }
    result = switch.get(user_selection)
    result()
