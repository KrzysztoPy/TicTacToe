def number_of_players():
    init_create_players(
        main_menu_func.selecting_from_available_options(player_text.how_many_player_text()[0],
                                                        len(player_text.how_many_player_text()[1]),
                                                        player_text.how_many_player_text(),
                                                        main_menu_text.question_about_selected_option_text()))
