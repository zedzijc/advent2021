from solutions.common.parse import parse_input_as_list, parse_coordinates
from solutions.common.coordinate import Coordinate


def count_overlapping_lines(puzzle_input):
	print ("Number of overlapping lines: {0}".format(
		_determine_overlapping_lines(puzzle_input)))


def _determine_overlapping_lines(puzzle_input):
	markings = {}
	coordinates = _process_coordinates(parse_input_as_list(puzzle_input))
	for coordinate_pair in coordinates:
		for line_coordinate in _get_line_coordinates(coordinate_pair):
			if line_coordinate not in markings:
				markings[line_coordinate] = 1
			else:
				markings[line_coordinate] += 1

	return len([value for value in markings.values() if value >= 2])


def _process_coordinates(puzzle_input):
	coordinates = []
	for input_line in puzzle_input:
		coordinates.append(parse_coordinates(input_line))
	return coordinates


def _get_line_coordinates(coordinate_pair):
	line_coordinates = []
	coord_a = coordinate_pair[0]
	coord_b = coordinate_pair[1]

	if coord_a == coord_b:
		line.coordinates.append(Coordinate(coord_a.x, coord_a.y))

	elif coord_a.x == coord_b.x: # Horizontal
		y_coordinates = [coord_a.y, coord_b.y]
		for y_coordinate in range(min(y_coordinates), max(y_coordinates) + 1):
			line_coordinates.append(Coordinate(coord_a.x, y_coordinate))
	elif coord_a.y == coord_b.y: # Vertical
		x_coordinates = [coord_a.x, coord_b.x]
		for x_coordinate in range(min(x_coordinates), max(x_coordinates) + 1):
			line_coordinates.append(Coordinate(x_coordinate, coord_a.y))
	else: #Diagonal 45 degrees
		x = coord_a.x
		y = coord_a.y
		if (coord_a.x > coord_b.x and coord_a.y > coord_b.y):
			while coord_b not in line_coordinates:
				line_coordinates.append(Coordinate(x,y))
				x -= 1
				y -= 1

		elif (coord_a.x < coord_b.x and coord_a.y < coord_b.y):
			while coord_b not in line_coordinates:
				line_coordinates.append(Coordinate(x,y))
				x += 1
				y += 1
		elif (coord_a.x > coord_b.x):
			while coord_b not in line_coordinates:
				line_coordinates.append(Coordinate(x,y))
				x -= 1
				y += 1
		else:
			while coord_b not in line_coordinates:
				line_coordinates.append(Coordinate(x,y))
				x += 1
				y -= 1

	return line_coordinates