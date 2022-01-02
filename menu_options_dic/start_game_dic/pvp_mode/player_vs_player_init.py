from player_dic.player_class import Player


def player_vs_player_init():
    player_one = Player()
    player_two = Player()

    set_players_name(player_one, player_two)


def set_players_name(player_one, player_two):
    player_one.setting_name_of_the_players()
    player_two.setting_name_of_the_players()



