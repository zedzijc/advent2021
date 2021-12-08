from solutions.common.parse import parse_input_as_list


def find_unique_number_occurences(puzzle_input):
	output_values = _get_output_values(parse_input_as_list(puzzle_input))

	pattern_lengths = [2,3,4,7]
	hits = 0
	for output_value in output_values:
		for value in output_value:
			if len(value) in pattern_lengths:
				hits += 1
	print ("Number 1 4 7 8 occurs {0} times in output values".format(hits))


def find_output_value_sums(puzzle_input):
	output_sum = 0
	for input_output_values in _get_input_output_values(parse_input_as_list(puzzle_input)):
		input_values = _decode_input_values(input_output_values[0])
		output_sum += _get_output_values_sum(input_values, input_output_values[1])
	print("Total output sum: {0}".format(output_sum))


def _decode_input_values(input_values):
	decoded_input_values = [
		"",
		_decode_unique_number(input_values, 2),
		"",
		"",
		_decode_unique_number(input_values, 4),
		"",
		"",
		_decode_unique_number(input_values, 3),
		_decode_unique_number(input_values, 7),
		""]
	decoded_input_values[6] = _decode_six(input_values, decoded_input_values[1])
	decoded_input_values[0] = _decode_zero(input_values, decoded_input_values[1], decoded_input_values[4])
	decoded_input_values[9] = _decode_remaining_number(input_values, 6)
	decoded_input_values[3] = _decode_three(input_values, decoded_input_values[1])
	decoded_input_values[2] = _decode_two(input_values, decoded_input_values[9])
	decoded_input_values[5] = _decode_remaining_number(input_values, 5)
	return decoded_input_values


def _get_output_values_sum(input_values, output_values):
	output_string_sum = ""
	for output_value in output_values:
		for index, input_value in enumerate(input_values):
			if sorted(output_value) == sorted(input_value):
				output_string_sum += str(index)
				break
	return int(output_string_sum)


def _decode_unique_number(input_values, length):
	for index, input_value in enumerate(input_values):
		if len(input_value) == length:
			del input_values[index]
			return input_value


def _decode_six(input_values, one):
	for index, input_value in enumerate(input_values):
		if len(input_value) == 6 and _does_not_contain_number(input_value, one):
			del input_values[index]
			return input_value


def _decode_zero(input_values, one, four):
	for index, input_value in enumerate(input_values):
		if len(input_value) == 6 and _does_not_contain_number(input_value, four):
			del input_values[index]
			return input_value


def _decode_three(input_values, one):
	for index, input_value in enumerate(input_values):
		if len(input_value) == 5 and _contains_number(input_value, one):
			del input_values[index]
			return input_value

def _decode_two(input_values, nine):
	for index, input_value in enumerate(input_values):
		if len(input_value) == 5:
			for value in input_value:
				if value not in nine:
					del input_values[index]
					return input_value


# Assumes all other numbers of similar length were removed first.
def _decode_remaining_number(input_values, length):
	for index, input_value in enumerate(input_values):
		if len(input_value) == length:
			del input_values[index]
			return input_value


def _contains_number(input_value, contained_value):
	for value in contained_value:
		if value not in input_value:
			return False
	return True


def _does_not_contain_number(input_value, contained_value):
	for value in contained_value:
		if value not in input_value:
			return True
	return False


def _get_input_output_values(puzzle_lines):
	input_output_values = []
	for line in puzzle_lines:
		input_output_values.append([_get_single_input_values(line), _get_single_output_values(line)])
	return input_output_values


def _get_single_output_values(puzzle_line):
	return puzzle_line.split('|')[1].strip().split(" ")


def _get_single_input_values(puzzle_line):
	return puzzle_line.split('|')[0].strip().split(" ")


def _get_output_values(puzzle_lines):
	output_values = []
	for line in puzzle_lines:
		output_values.append(line.split('|')[1].split(" "))
	return output_values
