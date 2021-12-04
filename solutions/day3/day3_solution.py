from solutions.common.parse import parse_input_as_binary_list


def find_power_consumption(puzzle_input):
    print("Power consumption is: {0}".format(
        _calculate_power_consumption(
            parse_input_as_binary_list(puzzle_input))))


def find_life_support_rating(puzzle_input):
    binary_input = parse_input_as_binary_list(puzzle_input)
    print("Life support rating is: {0}".format(
        _get_life_support_sub_ratings(binary_input, True)
        * _get_life_support_sub_ratings(binary_input, False)))


def _calculate_power_consumption(bit_patterns):
    bit_mask = int('0000100000000000', 2)
    gamma_rate = int('0000000000000000', 2)
    epsilon_rate = int('0000000000000000', 2)
    majority_threshold = len(bit_patterns) / 2

    while bit_mask > 0:
        counter = 0
        for bit_pattern in bit_patterns:
            counter += 1 if bit_mask & bit_pattern else 0

        if counter > majority_threshold:
            gamma_rate = gamma_rate | bit_mask
        else:
            epsilon_rate = epsilon_rate | bit_mask

        bit_mask = bit_mask >> 1

    print(gamma_rate, epsilon_rate)
    return gamma_rate * epsilon_rate


def _get_life_support_sub_ratings(bit_patterns,
                                  oxygen,
                                  bit_mask=int('0000100000000000', 2)):
    high_patterns = []
    low_patterns = []
    if len(bit_patterns) == 1:
        return bit_patterns[0]

    for bit_pattern in bit_patterns:
        for bit_pattern in bit_patterns:
            if bit_mask & bit_pattern:
                high_patterns.append(bit_pattern)
            else:
                low_patterns.append(bit_pattern)
        bit_mask = bit_mask >> 1
        if oxygen:
            if len(high_patterns) >= len(low_patterns):
                return _get_life_support_sub_ratings(
                    high_patterns,
                    oxygen,
                    bit_mask)
            else:
                return _get_life_support_sub_ratings(
                    low_patterns,
                    oxygen,
                    bit_mask)
        else:
            if len(high_patterns) >= len(low_patterns):
                return _get_life_support_sub_ratings(
                    low_patterns,
                    oxygen,
                    bit_mask)
            else:
                return _get_life_support_sub_ratings(
                    high_patterns,
                    oxygen,
                    bit_mask)
