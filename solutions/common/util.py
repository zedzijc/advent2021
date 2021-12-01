def strings_to_integers(strings):
    integers = []
    for string in strings:
        try:
            integers.append(int(string))
        except TypeError:
            pass
    return integers