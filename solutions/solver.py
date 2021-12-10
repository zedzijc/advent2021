from solutions.day1.day1_solution import find_depth_increases, find_sliding_depth_increases
from solutions.day2.day2_solution import find_horizontal_depth_multiplier
from solutions.day3.day3_solution import find_power_consumption, find_life_support_rating
from solutions.day4.day4_solution import play_bingo
from solutions.day5.day5_solution import count_overlapping_lines
from solutions.day6.day6_solution import model_cuttlefish
from solutions.day7.day7_solution import find_lowest_fuel_position
from solutions.day8.day8_solution import find_unique_number_occurences, find_output_value_sums
from solutions.day10.day10_solution import syntax_error_score

solutions = {1: {1: find_depth_increases,
                 2: find_sliding_depth_increases},
             2: {1: find_horizontal_depth_multiplier,
                 2: find_horizontal_depth_multiplier},
             3: {1: find_power_consumption,
                 2: find_life_support_rating},
             4: {1: play_bingo,
                 2: play_bingo},
             5: {1: count_overlapping_lines,
                 2: count_overlapping_lines},
             6: {1: model_cuttlefish,
                 2: model_cuttlefish},
             7: {1: find_lowest_fuel_position,
                 2: find_lowest_fuel_position},
             8: {1: find_unique_number_occurences,
                 2: find_output_value_sums},
             9: {},
             10: {1: syntax_error_score},
             11: {},
             12: {},
             13: {},
             14: {},
             15: {},
             16: {},
             17: {},
             18: {},
             19: {},
             20: {},
             21: {},
             22: {},
             23: {},
             24: {}}


def has_solution(day, puzzle):
    return day in solutions and puzzle in solutions[day]


def solve(day, puzzle, puzzle_input):
    if has_solution(day, puzzle):
        if puzzle_input is None:
            solutions[day][puzzle]()
        else:
            solutions[day][puzzle](puzzle_input)
    else:
        print("Combination of Day: {0} and Puzzle: {1} "
              "is not yet implemented".format(day, puzzle))
