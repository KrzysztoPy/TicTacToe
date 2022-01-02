import player_dic.player_class_text as player_text
import main_menu_dic.main_menu as main_menu_func
import main_menu_dic.main_menu_text as main_menu_text

from pynput import keyboard
from random import randint


class Player:
    player_number = 1
    button_pressed = None

    def __init__(self):
        self.__id = 'Player ' + str(Player.player_number)
        self.__name = ''
        self.__score = ''
        Player.player_number += 1

    def __str__(self):
        return f'{self.__class__.__name__}(id:{self.id},name:{self.name},score:{self.score})'

    def __repr__(self):
        return f'{self.__class__.__name__}()'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @staticmethod
    def set_input(output_information):
        return input(output_information)

    @staticmethod
    def displaying_text_to_user(text_for_display):
        print(text_for_display)

    def setting_name_of_the_players(self):
        while True:
            self.name = Player.set_input(player_text.set_player_name_text(self.id))

            if self.check_if_the_player_name_is_empty() is True:
                self.check_if_and_convert_player_name_if_has_empty_field_and_spaces_to_underline()
                if self.accepting_the_selected_username():
                    break

    def check_if_the_player_name_is_empty(self):
        if self.name == '' or self.name.replace(' ', '') == '':
            Player.displaying_text_to_user(player_text.player_name_is_empty_text())
            return False
        else:
            Player.displaying_text_to_user(self.name)
            return True

    def check_if_and_convert_player_name_if_has_empty_field_and_spaces_to_underline(self):
        if ' ' in self.name:
            Player.displaying_text_to_user(player_text.rules_for_creating_player_name_text())
            self.name = self.name.replace(' ', '_')

    def accepting_the_selected_username(self):
        Player.displaying_text_to_user(player_text.want_keep_the_player_name_text(self.name))
        Player.displaying_text_to_user(player_text.selected_option_text())
        Player.create_keyboard_listener()

        if Player.button_pressed == 'y' or Player.button_pressed == 'Y':
            return True

        if Player.button_pressed == 'n' or Player.button_pressed == 'N':
            return False

    @staticmethod
    def create_keyboard_listener():
        listener = keyboard.Listener(on_press=Player.on_press)
        listener.start()
        listener.join()

    @staticmethod
    def on_press(key):
        if key == keyboard.KeyCode.from_char(chr(110)) or key == keyboard.KeyCode.from_char(chr(78)):
            Player.button_pressed = 'n'
            return False
        elif key == keyboard.KeyCode.from_char(chr(121)) or key == keyboard.KeyCode.from_char(chr(89)):
            Player.button_pressed = 'y'
            return False
        else:
            Player.displaying_text_to_user(player_text.invalid_press_button_text())
            Player.displaying_text_to_user(player_text.selected_option_text())
            return True


class Computer_Player(Player):
    pc_names = ['Fugaku', 'Summit', 'Sierra', 'Sunway', 'Tianhe-2']

    def __init__(self):
        super().__init__()
        self.set_name_for_computer()

    def __repr__(self):
        super().__repr__()

    def set_name_for_computer(self):
        self.name = randint(0, Computer_Player.pc_names.__len__() + 1)
