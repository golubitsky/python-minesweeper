from src import board, view
import pytest

def test_new_board_printed_all_empty(capsys):
    # arrange
    board_input = board.Board(2)
    sut = view.View(board_input)
    
    # act
    actual = sut.print()
    
    # assert
    out, err = capsys.readouterr()
    assert out == '_ _\n_ _\n'