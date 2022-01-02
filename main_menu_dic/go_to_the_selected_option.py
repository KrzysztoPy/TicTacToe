from menu_options_dic.start_game_dic.game_mode import *
from menu_options_dic.exit_game_dic.exit_game import exit_game


def go_to_the_selected_option(user_selection):
    switch = {
        1: init_create_players,
        2: lambda: 2,
        3: exit_game
    }
    result = switch.get(user_selection)
    result()
