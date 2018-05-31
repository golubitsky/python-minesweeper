import random
import os
from src import constants
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
        self.board = self._create_board_with_mines(size, n_mines)
        self._insert_values_into_board()

    def _create_board_with_mines(self, size, n_mines):
        board = [None for x in range(size ** 2)]
        mine_indices = set(random.sample(range(len(board)), n_mines))        
        for i in range(len(board)):
            board[i] = Cell()
            if i in mine_indices:
                board[i].mine = True

        return board
    
    def _insert_values_into_board(self):
        for i in range(len(self.board)):
            if not self.board[i].mine:
                self.board[i].n_surrounding_mines = self._count_adjacent_mines(i)

    def _is_in_bounds(self, y, x):
        if y < 0 or y >= self._size:
            return False
        if x < 0 or x >= self._size:
            return False
        return True

    def _count_adjacent_mines(self, index):
        mine_count = 0

        y, x = self._to_coord(index)
        for vec_y, vec_x in constants.directions:
            adj_y, adj_x = y + vec_y, x + vec_x
            if not self._is_in_bounds(adj_y, adj_x):
                continue
            
            index = self._from_coord(adj_y, adj_x)
            if self.board[index].mine:
                mine_count += 1
        
        return mine_count

    def _to_coord(self, index):
        """
            The 2d board is stored as a 1d array.
            This function converts in index to a (y, x) tuple.
            Top-left corner = (0, 0)
            Bottom-right corner = (size - 1, size - 1)
        """
        return (index % self._size, index // self._size)
    
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