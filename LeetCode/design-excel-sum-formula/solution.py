class Excel:

    def __init__(self, height: int, width: str):
        width = ord(width) - ord('A') + 1
        self.matrix = [[0] * width for _ in range(height)]

    def set(self, row: int, column: str, val: int) -> None:
        row_idx, col_idx = row - 1, ord(column) - ord('A')
        self.matrix[row_idx][col_idx] = val

    def _get(self, formula) -> int:
        if isinstance(formula, int):
            return formula
        res = 0
        for cell in formula:
            if cell in self.calculated:
                res += self.calculated[cell]
                continue
            r, c = cell
            value = self._get(self.matrix[r][c])
            self.calculated[cell] = value
            res += value
        return res

    def get(self, row: int, column: str) -> int:
        row_idx, col_idx = row - 1, ord(column) - ord('A')
        self.calculated = dict()
        return self._get(self.matrix[row_idx][col_idx])

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        row_idx, col_idx = row - 1, ord(column) - ord('A')
        self.matrix[row_idx][col_idx] = []
        for number in numbers:
            if ':' not in number:
                c, r = ord(number[0]) - ord('A'), int(number[1:]) - 1
                self.matrix[row_idx][col_idx].append((r, c))
                continue
            start_cell, end_cell = number.split(':')
            c_start, r_start = ord(start_cell[0]) - ord('A'), int(start_cell[1:]) - 1
            c_end, r_end = ord(end_cell[0]) - ord('A'), int(end_cell[1:]) - 1
            for r in range(r_start, r_end + 1):
                for c in range(c_start, c_end + 1):
                    self.matrix[row_idx][col_idx].append((r, c))
        return self.get(row, column)


# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)