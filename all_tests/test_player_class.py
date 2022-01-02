# from player_dic.player_class import Player
from player_dic.player_class import Player, Computer_Player
from pynput import keyboard

#Must comment While True:
def test_number_of_players(monkeypatch):
    sample = ['z', '\FF', -1, 0, 1, 2, 3]
    for counter in range(len(sample)):
        monkeypatch.setattr('builtins.input', lambda _: sample[counter])
        Player.number_of_players()


def test_check_if_the_player_name_is_empty():
    test_player = Player()
    samples = ('', ' ', ' ||x | | ', '    BD |4# ')
    expected_result = (False, False, True, True)

    for counter in range(samples.__len__()):
        test_player.name = samples[counter]
        result = test_player.check_if_the_player_name_is_empty()
        assert result == expected_result[counter]


def test_check_if_and_convert_player_name_if_has_empty_field_and_spaces_to_underline():
    test_player = Player()
    samples = ('||X55V', ' 35 7 XX ^ ')
    expected_result = ('||X55V', '_35_7_XX_^_')

    for counter in range(samples.__len__()):
        test_player.name = samples[counter]
        test_player.check_if_and_convert_player_name_if_has_empty_field_and_spaces_to_underline()
        assert test_player.name == expected_result[counter]


def test_accepting_the_selected_username():
    player = Player()
    player.accepting_the_selected_username()


def test_create_keyboar_listener():
    # Player.create_keyboar_listener()
    samples = (
        keyboard.KeyCode.from_char(chr(65)), keyboard.KeyCode.from_char(chr(77)), keyboard.KeyCode.from_char(chr(88)),
        keyboard.KeyCode.from_char(chr(100)), keyboard.KeyCode.from_char(chr(108)), keyboard.KeyCode.from_char(chr(89)),
        keyboard.KeyCode.from_char(chr(78)), keyboard.KeyCode.from_char(chr(121)), keyboard.KeyCode.from_char(chr(110)))
    expected_result = (True, True, True, True, True, False, False, False, False)
    for counter in range(samples.__len__()):
        result = Player().on_press(samples[counter])
        assert result == expected_result[counter]

def test_init_create_players():
    first_computer = Computer_Player()
    first_computer
