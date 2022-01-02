from another_func_dic.view_text_in_console import set_input


def test_set_input():
    set_input('text without separator')
    set_input(['text', 'with', 'separator'], ' -- ')
