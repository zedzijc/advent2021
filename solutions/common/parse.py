from solutions.common.util import strings_to_integers, strings_to_binary
from solutions.common.coordinate import Coordinate
import csv
import re


def parse_csv_to_list(puzzle_input):
    with open(puzzle_input, 'r') as csv_file:
        return(list(csv.reader(csv_file))[0])


def parse_input_as_list(puzzle_input):
    return open(puzzle_input).read().splitlines()


def parse_input_as_integer_list(puzzle_input):
    return strings_to_integers(parse_input_as_list(puzzle_input))


def parse_input_as_binary_list(puzzle_input):
    return strings_to_binary(parse_input_as_list(puzzle_input))


def parse_coordinates(string):
    pattern = "[0-9]+,[0-9]+"
    coordinates = []

    for raw_coord in re.findall(pattern, string):
        split_coord = raw_coord.split(',')
        coordinates.append(Coordinate(int(split_coord[0]), int(split_coord[1])))
    return coordinates