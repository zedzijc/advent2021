from solutions.common.parse import parse_input_as_list


def find_horizontal_depth_multiplier(puzzle_input):
    print("multiplied value is: {0}".format(
        _calculate_horizontal_depth_multiplier(
            parse_input_as_list(puzzle_input))))


def _calculate_horizontal_depth_multiplier(raw_instructions):
    depth = 0
    horizontal_position = 0

    for raw_instruction in raw_instructions:
        instruction = _parse_instruction(raw_instruction)
        if instruction.direction == "up":
            depth -= instruction.value
        elif instruction.direction == "down":
            depth += instruction.value
        elif instruction.direction == "forward":
            horizontal_position += instruction.value
        else:
            print("got an unsupported instruction: {0} with value {1}".format(instruction.direction, instruction.value))
    return depth * horizontal_position


def _parse_instruction(instruction):
    raw_instruction = instruction.split(" ")
    return Instruction(raw_instruction[0], int(raw_instruction[1]))


class Instruction(object):

    def __init__(self, direction, value):
        self.direction = direction
        self.value = value
