from solutions.common.parse import parse_csv_to_list
from solutions.common.util import strings_to_integers


def model_cuttlefish(puzzle_input):
	days = 80
	respawn_time = 7
	print("Number of cuttlefish after {0} days: {1}".format(
		days, _run_cuttlefish_model(strings_to_integers(parse_csv_to_list(puzzle_input)), respawn_time, days)))

def _run_cuttlefish_model(cuttlefish, respawn_time, days):
	cuttlefish_distribution = _determine_initial_cuttlefish_distribution(cuttlefish, respawn_time)
	
	day = 0
	while day < days:
		cuttlefish_distribution = _process_cuttlefish_day(cuttlefish_distribution, respawn_time)
		day += 1

	cuttlefish_total = 0
	for cuttlefish_group in cuttlefish_distribution:
		cuttlefish_total += cuttlefish_group
	return cuttlefish_total

def _process_cuttlefish_day(cuttlefish_distribution, respawn_time):
	new_distribution = _get_empty_cuttlefish_distribution(respawn_time)
	for index, cuttlefish_group in enumerate(cuttlefish_distribution):
		if index == 0:
			new_distribution[len(new_distribution) -1 ] += cuttlefish_group
			new_distribution[respawn_time -1 ] += cuttlefish_group
		else:
			new_distribution[index - 1] += cuttlefish_group
	return new_distribution

def _determine_initial_cuttlefish_distribution(cuttlefish, respawn_time):
	cuttlefish_distribution = _get_empty_cuttlefish_distribution(respawn_time)
	for one_cuttlefish in cuttlefish:
		cuttlefish_distribution[one_cuttlefish] += 1
	return cuttlefish_distribution


def _get_empty_cuttlefish_distribution(respawn_time):
	return [0 for x in range(respawn_time + 2)]