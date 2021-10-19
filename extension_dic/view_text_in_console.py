def set_input(input_text, separator=None):
    if separator is None:
        print(input_text)
    else:
        print(*input_text, sep=separator)

