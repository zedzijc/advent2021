from solutions.day4.bingo_board import BingoBoard

BINGO_NUMBERS = [15,61,32,33,87,17,56,73,27,83,0,18,43,8,86,37,40,6,93,25,14,68,64,57,39,46,55,13,21,72,51,81,78,79,52,65,36,92,97,28,9,24,22,69,70,42,3,4,63,50,91,16,41,94,77,85,49,12,76,67,11,62,99,54,95,1,74,34,88,89,82,48,84,98,58,44,5,53,7,19,29,30,35,26,31,10,60,59,80,71,45,38,20,66,47,2,23,96,90,75]


def play_bingo(puzzle_input):
    winning_board_scores = []
    bingo_boards = _setup_boards(puzzle_input)
    for number in BINGO_NUMBERS:
        boards_with_bingo = []
        for board_index, board in enumerate(bingo_boards):
            score = board.mark_number(number)
            if score:
                if len(bingo_boards) == 1:
                    winning_board_scores.append(score)
                else:
                    boards_with_bingo.append(board_index)
        boards_with_bingo.reverse()
        for board_index in boards_with_bingo:
            bingo_boards.pop(board_index)
        if winning_board_scores:
            break
    print("Winning board score: {0}".format(
        max(winning_board_scores)))


def _setup_boards(puzzle_input):
    bingo_boards = []
    for matrix in _parse_input_as_matrices(puzzle_input):
        bingo_boards.append(BingoBoard(matrix))
    return bingo_boards

def _parse_input_as_matrices(puzzle_input):
    matrices = [[]]
    for row in parse_input_as_list(puzzle_input):
        if row:
            matrices[len(matrices) - 1].append(numbers_to_bingo_numbers(strings_to_integers(row.strip().replace("  ", " ").split(" "))))
        else:
            matrices.append(list())
    return matrices