import random
import os
from math import sqrt
from src import constants
import platform

class View():
    def __init__(self, board_class):
        self._view = self._convert_to_view(board_class.board)
        self._size = int(sqrt(len(board_class.board)))

    def clear(self):
        clear_cmd = 'cls' if platform.system() == 'Windows' else 'clear'
        _ = os.system(clear_cmd)

    def print(self):
        self.clear()

        x_labels = " ".join(map(str, list(range(self._size))))
        print("  " + x_labels)
        for y in range(self._size):
            y_label = f"{y} "
            line = y_label
            for x in range(self._size):
                cell = self._view[y * self._size + x]
                line += f"{cell} "
            print(line.strip())

    def _convert_to_view(self, board):
        # never allow modification of actual board
        view = [None] * len(board)
        
        for i in range(len(board)):
            cell = board[i]
            if cell.flagged:
                view[i] = constants.display_char_flagged
            elif cell.revealed and cell.mine:
                view[i] = constants.display_char_mine
            elif cell.revealed:
                view[i] = cell.n_surrounding_mines
            else:
                view[i] = constants.display_char_unrevealed
        
        return view