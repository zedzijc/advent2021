from solutions.common.util import strings_to_integers, strings_to_binary
from solutions.day4.bingo_number import numbers_to_bingo_numbers
import csv


def parse_csv_to_list(puzzle_input):
    with open(puzzle_input, 'r') as csv_file:
        return(list(csv.reader(csv_file)))


def parse_input_as_list(puzzle_input):
    return open(puzzle_input).read().splitlines()


def parse_input_as_integer_list(puzzle_input):
    return strings_to_integers(parse_input_as_list(puzzle_input))


def parse_input_as_binary_list(puzzle_input):
    return strings_to_binary(parse_input_as_list(puzzle_input))


def parse_input_as_matrices(puzzle_input):
    matrices = [[]]
    for row in parse_input_as_list(puzzle_input):
        if row:
            matrices[len(matrices) - 1].append(numbers_to_bingo_numbers(strings_to_integers(row.strip().replace("  ", " ").split(" "))))
        else:
            matrices.append(list())
    return matrices
