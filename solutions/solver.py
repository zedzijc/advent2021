from solutions.day1.day1_solution import find_depth_increases, find_sliding_depth_increases
from solutions.day2.day2_solution import find_horizontal_depth_multiplier
from solutions.day3.day3_solution import find_power_consumption, find_life_support_rating


solutions = {1: {1: find_depth_increases,
                 2: find_sliding_depth_increases},
             2: {1: find_horizontal_depth_multiplier,
                 2: find_horizontal_depth_multiplier},
             3: {1: find_power_consumption,
                 2: find_life_support_rating},
             4: {},
             5: {},
             6: {},
             7: {},
             8: {},
             9: {},
             10: {},
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
