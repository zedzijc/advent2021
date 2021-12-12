from solutions.common.parse import parse_input_as_list
from solutions.common.coordinate import Coordinate


def low_points_sum(puzzle_input):
    risk_level_sum = 0
    lines = parse_input_as_list(puzzle_input)
    for line_index, line in enumerate(lines):
        for point_index, point in enumerate(line):
            up = True
            down = True
            left = True
            right = True

            if line_index - 1 >= 0:
                up = point < lines[line_index - 1][point_index]

            if point_index - 1 >= 0:
                left = point < line[point_index - 1]

            if point_index < len(line) - 1:
                right = point < line[point_index + 1]

            if line_index < len(lines) - 1:
                down = point < lines[line_index + 1][point_index]

            if up and down and left and right:
                risk_level_sum += int(point) + 1
    print("Risk level sum is: {0}".format(risk_level_sum))


def basin_sums(puzzle_input):
    VISITED_COORDINATES = set()
    lines = parse_input_as_list(puzzle_input)
    #  Mark all 9s as visited, to utilize them as borders
    for line_index, line in enumerate(lines):
        for point_index, point in enumerate(line):
            coord = Coordinate(point_index, line_index)
            if point == "9":
                VISITED_COORDINATES.add(coord)
    #  Scan all points for basins
    basin_coordinates = set()
    basin_sizes = []
    for line_index, line in enumerate(lines):
        for point_index, point in enumerate(line):
            _explore_basin(Coordinate(point_index, line_index), lines, basin_coordinates, VISITED_COORDINATES)
            if basin_coordinates:
                VISITED_COORDINATES = VISITED_COORDINATES | basin_coordinates
                basin_sizes.append(len(basin_coordinates))
                basin_coordinates.clear()
    basin_sizes.sort()
    largest_basins = basin_sizes[-3:]
    print("Basin total is: {0}".format(
        largest_basins[0] * largest_basins[1] * largest_basins[2]))


def _explore_basin(coordinate, lines, basin_coordinates, VISITED_COORDINATES):
    if coordinate in basin_coordinates or coordinate in VISITED_COORDINATES:
        return
    basin_coordinates.add(coordinate)
    coords = set()

    if coordinate.y - 1 >= 0:
        coords.add(Coordinate(coordinate.x, coordinate.y - 1))

    if coordinate.x - 1 >= 0:
        coords.add(Coordinate(coordinate.x - 1, coordinate.y))

    if coordinate.x < len(lines[coordinate.y]) - 1:
        coords.add(Coordinate(coordinate.x + 1, coordinate.y))

    if coordinate.y < len(lines) - 1:
        coords.add(Coordinate(coordinate.x, coordinate.y + 1))

    for coord in coords:
        _explore_basin(coord, lines, basin_coordinates, VISITED_COORDINATES)
