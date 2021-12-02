from solutions.common.parse import parse_input_as_integer_list


def find_depth_increases(puzzle_input):
    print("Number of depth increases: {0}".format(
        _count_depth_increases(parse_input_as_integer_list(puzzle_input))))

def find_sliding_depth_increases(puzzle_input):
    print("Number of sliding depth increases: {0}".format(
        _count_sliding_depth_increases(parse_input_as_integer_list(puzzle_input))))


def _count_depth_increases(depth_readings):
    depth_increases = 0
    previous_depth_reading = depth_readings[0]
    for depth_reading in depth_readings[1:]:
        if depth_reading > previous_depth_reading:
            depth_increases += 1
        previous_depth_reading = depth_reading
    return depth_increases

def _count_sliding_depth_increases(depth_readings):
    depth_increases = 0
    index = 3
    while index <= len(depth_readings):
        if sum(depth_readings[index-3: index]) < sum(depth_readings[index-2: index+1]):
            depth_increases += 1
        index += 1
    return depth_increases
