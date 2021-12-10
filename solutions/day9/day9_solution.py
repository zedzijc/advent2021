from solutions.common.parse import parse_input_as_list


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
