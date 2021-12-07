from solutions.common.util import strings_to_integers
from solutions.common.parse import parse_csv_to_list


def find_lowest_fuel_position(puzzle_input):
	positions = strings_to_integers(parse_csv_to_list(puzzle_input))
	rough_granularity = 100
	hundredth, _ = _calculate_by_granularity(positions, rough_granularity, 0, len(positions))
	_ , fuel_sum = _calculate_by_granularity(positions, 1, hundredth - rough_granularity, hundredth + rough_granularity)
	print ("Lowest fuel_sum is: {0}".format(fuel_sum))


def _calculate_by_granularity(positions, granularity, lower_bound, upper_bound):
	value = lower_bound
	out_of_bounds = upper_bound
	lowest_fuel_sum = out_of_bounds * len(positions)
	lowest_value = out_of_bounds
	while value < out_of_bounds:
		value_sum = 0
		for position in positions:
			value_sum += abs(position-value)
		if value_sum < lowest_fuel_sum:
			lowest_fuel_sum = value_sum
			lowest_value = value
		value += granularity
	return lowest_value, lowest_fuel_sum


