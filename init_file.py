from main_menu_dic.main_menu import selecting_from_available_options
from main_menu_dic.main_menu_text import menu_option_text, question_about_selected_option_text
from main_menu_dic.go_to_the_selected_option import go_to_the_selected_option

selected_option = selecting_from_available_options(menu_option_text()[0], len(menu_option_text()[1]),
                                                   menu_option_text()[1], question_about_selected_option_text())
go_to_the_selected_option(selected_option)

#nothing