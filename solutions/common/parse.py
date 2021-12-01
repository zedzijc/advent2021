from solutions.common.util import strings_to_integers
import csv

def parse_csv_to_list(puzzle_input):
    with open(puzzle_input, 'r') as csv_file:
        return(list(csv.reader(csv_file)))


def parse_input_as_list(puzzle_input):
    return open(puzzle_input).read().splitlines()

def parse_input_as_integer_list(puzzle_input):
    return strings_to_integers(parse_input_as_list(puzzle_input))