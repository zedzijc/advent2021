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

def _get_output_values(puzzle_lines):
	output_values = []
	for line in puzzle_lines:
		output_values.append(line.split('|')[1].split(" "))
	return output_values
