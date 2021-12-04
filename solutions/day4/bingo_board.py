import copy

class BingoBoard(object):

    def __init__(self, bingo_rows):
        self.bingo_rows = copy.deepcopy(bingo_rows)

    def mark_number(self, number):
        for row_index, row in enumerate(self.bingo_rows):
            for column_index, row_number in enumerate(row):
                if row_number == number:
                    row_number.marked = True
                    if self._has_bingo(row_index, column_index):
                        return self._get_bingo_score(number)
                    else:
                        return 0

    def _has_bingo(self, row_index, column_index):
        for number in self.bingo_rows[row_index]:
            if not number.marked:
                return False
        for row in self.bingo_rows:
            if not row[column_index].marked:
                return False
        return True

    def _get_bingo_score(self, number):
        unmarked_sum = 0
        for row in self.bingo_rows:
            for row_number in row:
                if not row_number.marked:
                    unmarked_sum += row_number.number
        return unmarked_sum * number
