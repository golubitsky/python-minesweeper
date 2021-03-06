import random
import os
from math import sqrt
from src import constants


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
        board = [None for x in range(size**2)]
        mine_indices = set(random.sample(range(len(board)), n_mines))
        for i in range(len(board)):
            board[i] = Cell()
            if i in mine_indices:
                board[i].mine = True

        return board

    def _insert_values_into_board(self):
        for i in range(len(self.board)):
            if not self.board[i].mine:
                self.board[i].n_surrounding_mines = self._count_adjacent_mines(
                    i)

    def _is_in_bounds(self, y, x):
        if y < 0 or y >= self._size:
            return False
        if x < 0 or x >= self._size:
            return False
        return True

    def _get_adjacent_indices(self, index):
        y, x = self._to_coord(index)
        indices = []
        for vec_y, vec_x in constants.directions:
            adj_y, adj_x = y + vec_y, x + vec_x
            if not self._is_in_bounds(adj_y, adj_x):
                continue

            index = self._from_coord(adj_y, adj_x)
            indices.append(index)

        return indices

    def _count_adjacent_mines(self, index):
        adjacent_indices = self._get_adjacent_indices(index)
        mine_count = 0

        for adj_index in adjacent_indices:
            if self.board[adj_index].mine:
                mine_count += 1

        return mine_count

    def _to_coord(self, index):
        """
            The 2d board is stored as a 1d array.
            This function converts in index to a (y, x) tuple.
            Top-left corner = (0, 0)
            Bottom-right corner = (size - 1, size - 1)
        """
        return (index // self._size, index % self._size)

    def _from_coord(self, y, x):
        """
            The 2d board is stored as a 1d array.
            This function returns the index in the board given x and y.
        """
        return self._size * y + x

    def _reveal_single(self, index, seen):
        cell = self.board[index]
        cell.revealed = True
        seen.add(index)

    def _reveal_recursively(self, index, seen):
        if not self.board[index].mine:
            self._reveal_single(index, seen)

        for adjacent_index in self._get_adjacent_indices(index):
            adj_mine_count = self._count_adjacent_mines(adjacent_index)
            if adj_mine_count > 0 or adjacent_index in seen:
                continue
            self._reveal_recursively(adjacent_index, seen)

    def reveal(self, y, x):
        """
            Reveal a cell at coord (y, x)
        """
        seen = set()
        start_index = self._from_coord(y, x)
        # always reveal the requested index (whether mine or not)
        # in recursion we will not reveal mines
        self._reveal_single(start_index, seen)
        self._reveal_recursively(start_index, seen)
        


    def toggle_flag(self, y, x):
        """
            Reveal a cell at coord (y, x)
        """
        cell = self.board[self._from_coord(y, x)]
        cell.flagged = not cell.flagged

    def lost(self):
        return any(
            mine.revealed
            for mine in filter(lambda cell: cell.mine, self.board))

    def won(self):
        # each non-mine is revealed
        return all(
            non_mine.revealed
            for non_mine in filter(lambda cell: not cell.mine, self.board))
