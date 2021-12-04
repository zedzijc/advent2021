class BingoNumber(object):

    def __init__(self, number):
        self.number = number
        self.marked = False

    def __eq__(self, someNumber):
        return self.number == someNumber


def numbers_to_bingo_numbers(numbers):
    return [BingoNumber(number) for number in numbers]
