import copy

class BingoBoard(object):

    def __init__(self, bingo_rows):
        self.bingo_rows = copy.deepcopy(bingo_rows)

    def mark_number(self, number):
        for row_index, row in enumerate(self.bingo_rows):
            for column_index, number_in_row in enumerate(row):
                if number_in_row == number:
                    number_in_row.marked = True
                    if self._has_bingo(row_index, column_index):
                        return self._get_bingo_score(number)
                    else:
                        return 0

    def _has_bingo(self, row_index, column_index):
        horizontal_bingo = True
        vertical_bingo = True
        for number in self.bingo_rows[row_index]:
            if not number.marked:
                horizontal_bingo = False
        for row in self.bingo_rows:
            if not row[column_index].marked:
                vertical_bingo = False
        return horizontal_bingo | vertical_bingo

    def _get_bingo_score(self, number):
        unmarked_sum = 0
        for row in self.bingo_rows:
            for number_in_row in row:
                if not number_in_row.marked:
                    unmarked_sum += number_in_row.number
        return unmarked_sum * number
