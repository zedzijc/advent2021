from solutions.common.parse import parse_input_as_binary_list


def find_power_consumption(puzzle_input):
    print("Power consumption is: {0}".format(
        _calculate_power_consumption(
            parse_input_as_binary_list(puzzle_input))))


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
            print('gamma')
            gamma_rate = gamma_rate | bit_mask
        else:
            print('epsilon')
            epsilon_rate = epsilon_rate | bit_mask

        bit_mask = bit_mask >> 1

    print(gamma_rate, epsilon_rate)
    return gamma_rate * epsilon_rate
