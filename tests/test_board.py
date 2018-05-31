from src import board
import pytest

@pytest.mark.parametrize("expected_size", [3,7,20])
def test_board_is_square_with_correct_dimensions(expected_size):
    # arrange
    sut = board.Board(expected_size)

    # act
    actual = sut.board

    # assert
    assert len(actual) == expected_size ** 2

def test_reveals_square():
    # arrange
    sut = board.Board(3)

    # act
    sut.reveal(1,2) # y, x
    actual = sut.board

    # assert
    assert actual[5].revealed == True
    
def test_flags_square():
    # arrange
    sut = board.Board(3)

    # act
    sut.toggle_flag(1,2) # y, x
    actual = sut.board

    # assert
    assert actual[5].flagged == True

def test_flag_of_square_is_toggled_back():
    # arrange
    sut = board.Board(3)

    # act
    sut.toggle_flag(1, 2)
    sut.board[5].flagged = True
    sut.toggle_flag(1,2)

    # assert
    assert sut.board[5].flagged == False