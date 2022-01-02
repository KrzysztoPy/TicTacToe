from menu_options_dic.start_game_dic.pvp_mode import player_vs_player_init
from menu_options_dic.start_game_dic.pvc_mode import player_vs_computer_init


def init_create_players(selected_option):
    switch = {
        1: player_vs_player_init,
        2: player_vs_computer_init
    }
    create_players = switch.get(selected_option)
    create_players()
