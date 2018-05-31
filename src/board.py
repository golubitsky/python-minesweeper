import random
import os
from src.constants import *
from math import sqrt

class Cell():
    def __init__(self):
        self.n_surrounding_mines = 0
        self.mine = False
        self.revealed = False
        self.flagged = False

class Board():
    def __init__(self, size, n_mines=3):
        self._size = size
        self.board = self._create_random_board(size, n_mines)

    def _create_random_board(self, size, n_mines):
        board = [None for x in range(size ** 2)]
        mine_indices = set(random.sample(range(len(board)), n_mines))        
        for i in range(len(board)):
            board[i] = Cell()
            if i in mine_indices:
                board[i].mine = True

        return board
    
    def _count_adjacent_mines(self, index):
        pass

    def _to_coord(self, index_in_board):
        """
            The 2d board is stored as a 1d array.
            This function converts in index to a (y, x) tuple.
            Top-left corner = (0, 0)
            Bottom-right corner = (size - 1, size - 1)
        """
        return (index_in_board % self._size, index_in_board // self._size)
    
    def _from_coord(self, y, x):
        """
            The 2d board is stored as a 1d array.
            This function returns the index in the board given x and y.
        """
        return self._size * y + x
    
    def reveal(self, y, x):
        """
            Reveal a cell at coord (y, x)
        """
        cell = self.board[self._from_coord(y, x)]
        cell.revealed = True

    def toggle_flag(self, y, x):
        """
            Reveal a cell at coord (y, x)
        """
        cell = self.board[self._from_coord(y, x)]
        cell.flagged = not cell.flagged

    def lost(self):
        # each mine not revealed
        pass
    
    def won(self):
        # each non-mine is revealed
        pass